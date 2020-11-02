from pydap.client import open_url
import numpy as np


def generate_url(selected_date, satellite_number):
    base_url = "https://podaac-opendap.jpl.nasa.gov/opendap/hyrax/allData/cygnss/L1/v2.1/"
    date_string = str(selected_date.year) + str(selected_date.month).zfill(2) + str(selected_date.day).zfill(2)
    specific_url = "/cyg0" + str(
        satellite_number) + ".ddmi.s" + date_string + "-000000-e" + date_string + "-235959.l1.power-brcs.a21.d21.nc"
    opendap_url = base_url + str(selected_date.year) + "/" + str(selected_date.timetuple().tm_yday).zfill(3) + specific_url
    return opendap_url


def collect_dataset(url):
    dataset = open_url(url, output_grid=False)
    return dataset


def filter_valid_points(dataset, lat_min, lat_max, lon_min, lon_max):
    grid_data = []
    for ddm in range(4):
        sp_lat = np.array(dataset.sp_lat[:, ddm])
        sp_lon = np.array(dataset.sp_lon[:, ddm])
        for ddm_timestamp, latitude in enumerate(sp_lat):
            if lat_min <= latitude <= lat_max:
                longitude = sp_lon[ddm_timestamp][0]
                if lon_min <= longitude <= lon_max:
                    grid_data.append([latitude[0], longitude, ddm_timestamp, ddm])
    return grid_data


def separate_tracks(grid):
    track_list = []
    previous_timestamp = -9
    previous_ddm = -9
    current_track = []

    for measure in grid:
        if not previous_timestamp+1 == measure[2] or not measure[3] == previous_ddm:
            track_list.append(current_track)
            current_track = [measure]
        else:
            current_track.append(measure)

        previous_ddm = measure[3]
        previous_timestamp = measure[2]
    del track_list[0]
    track_list.append(current_track)

    return track_list
