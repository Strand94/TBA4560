from datetime import datetime
from apps.eddies.cygnss.opendap import *

# From user input:
test_date = datetime(2020, 10, 1)
lat = [25, 26]
lon = [144, 145]
min(lat)

#tests

url = generate_url(test_date, 1)
dataset = collect_dataset(url)
grid = filter_valid_points(dataset, min(lat), max(lat), min(lon), max(lon))
track_list = separate_tracks(grid)

print(len(track_list))
for track in track_list:
    print(len(track))

#grid = []
#count = 0
#specified_lat_lon = [25, 26, 167, 168]

#C = Cygnss(url)

#dataset = C.dataset

##cygnss_satellite = "1"
#for ddm in range(4):
#    sp_lat = np.array(dataset.sp_lat[:, ddm])
 #   sp_lon = np.array(dataset.sp_lon[:, ddm])
  #  for ddm_timestamp, latitude in enumerate(sp_lat):
   #     if 25 <= latitude <= 26:
    #        longitude = sp_lon[ddm_timestamp][0]
      #      if 25 <= longitude <= 26:
     #           grid.append([latitude[0], longitude, ddm_timestamp, ddm])

#print(grid)
#print(len(grid))
# Specular point latitude, in degrees North, at ddm_timestamp_utc
# print(dataset.sp_lat.shape)

# Specular point longitude, in degrees East, at ddm_timestamp_utc
# print(dataset.sp_lon.shape)

# Normalized BRCS of a 3 delay x 5 Doppler bin box that includes the specular point bin.
# print(dataset.ddm_nbrcs.shape)
