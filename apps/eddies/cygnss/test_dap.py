import pydap.client as pdc
import numpy as np
import cygnss
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# from pydap.cas.get_cookies import setup_session
# mySession = setup_session(authentication_url, username, password)

'''cyg = pdc.open_url(
    'https://opendap.jpl.nasa.gov/opendap/OceanWinds/cygnss/L1/v2.1/2020/100/cyg01.ddmi.s20200409-000000-e20200409-235959.l1.power-brcs.a21.d21.nc',
    output_grid=False)
t = cyg['ddm_timestamp_utc'][:]
t = np.tile(t.reshape((-1, 1)), (1, 4))'''


url = 'https://opendap.jpl.nasa.gov/opendap/OceanWinds/cygnss/L1/v2.1/2020/100/cyg01.ddmi.s20200409-000000-e20200409-235959.l1.power-brcs.a21.d21.nc'

C = cygnss.CygnssL1(url)
C.unique_track_id()
'''C.sp_latlon()
C.sp_time()'''

sig0 = C.retrieve_track(C.uidArray[50], 'sp_inc_angle')
sig0.along_track_coordinate()
sig0.make_grid_track(3000)

fig = plt.figure()
#ax = fig.gca(projection='3d')
ax = fig.gca()
#ax.plot(sig0.sp_lon, sig0.sp_lat, sig0.values)
ax.plot( sig0.grid_x, sig0.grid_y )
plt.show()
