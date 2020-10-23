import pydap.client as pdc
import numpy as np
from datetime import date
from geographiclib.geodesic import Geodesic
from scipy.interpolate import interp1d


class CygnssL1:
    def __init__(self, url):
        self.url = url
        self.content = pdc.open_url(url, output_grid=False)
        self.day = int(url.split('/')[-1].split('.')[2].split('-')[0][7:9])
        self.month = int(url.split('/')[-1].split('.')[2].split('-')[0][5:7])
        self.year = int(url.split('/')[-1].split('.')[2].split('-')[0][1:5])
        self.dayOfYear = int(url.split('/')[9])
        self.datenum = date.toordinal(date(self.year, self.month, self.day)) + 366

    def unique_track_id(self):

        spacecraft_num = np.array(self.content['spacecraft_num'][:])

        prn = np.array(self.content['prn_code'][:])

        track_id = np.array(self.content['track_id'][:])

        uid = self.datenum * 100000 + prn * 1000 + spacecraft_num + track_id / 100000

        self.uid = uid
        self.uidArray = np.unique(uid).reshape((-1, 1))

        return self.uidArray, uid

    def sp_latlon(self):
        self.sp_lat = np.array(self.content['sp_lat'][:])
        self.sp_lon = np.array(self.content['sp_lon'][:])

        return self.sp_lat, self.sp_lon

    def sp_time(self):
        secondOfDay = np.array(self.content['ddm_timestamp_utc'][:])
        self.secondOfDay = np.tile(secondOfDay.reshape(-1, 1), (1, 4))

        return self.secondOfDay

    def retrieve_track(self, trackUid, variableName):
        ind = self.uid == trackUid

        if not hasattr(self, 'sp_lat'):
            self.sp_latlon()

        if not hasattr(self, 'secondOfDay'):
            self.sp_time()

        sp_lat = self.sp_lat[ind]
        sp_lon = self.sp_lon[ind]
        time = self.datenum + self.secondOfDay[ind] / 86400

        i, j = np.where(ind)
        j = int(np.unique(j))
        start_i = np.min(i)
        end_i = np.max(i)+1
        values = self.content[variableName][start_i:end_i, j]


        values = np.reshape(values,(-1,))
        nanInd = values < 0
        values[nanInd] = np.NaN

        return CygnssTrack(trackUid, sp_lat, sp_lon, time, variableName, values)


class CygnssTrack:
    def __init__(self, trackUid, sp_lat, sp_lon, time, variableName, values):
        self.trackUid = trackUid
        self.sp_lat = sp_lat
        self.sp_lon = sp_lon
        self.time = time
        self.variableName = variableName
        self.values = values

    def along_track_coordinate(self):
        el = Geodesic.WGS84
        N = len(self.time)
        distance = [0]  # np.empty(N, )
        azimuth = []  # np.empty(N, )

        for i in range(0, N - 1):
            g = el.Inverse(self.sp_lat[i], self.sp_lon[i], self.sp_lat[i + 1], self.sp_lon[i + 1])
            distance.append(distance[-1] + g['s12'])
            azimuth.append(g['azi1'])

        azimuth.append(azimuth[-1])
        self.distance = np.array(distance)
        self.azimuth = np.array(azimuth)
        self.mean_distance = np.nanmean(np.diff(self.distance))
        self.mean_azimuth = np.nanmean(self.azimuth)

        return self.distance, self.azimuth

    def make_grid_track(self, gridStep):
        i = ~ np.isnan(self.values)
        f = interp1d(self.distance[i], self.values[i])
        x = np.arange(np.min(self.distance[i]), np.max(self.distance[i]), gridStep)
        y = f(x)
        self.grid_x = x
        self.grid_y = y

        return x, y
