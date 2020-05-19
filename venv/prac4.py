import cartopy
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

from opensky_api import OpenSkyApi


def coordinates():
    api = OpenSkyApi()
    lon = []
    lat = []
    j = 0
    # bbox = (min latitude, max latitude, min longitude, max longitude)
    states = api.get_states()  # bbox=(8.27, 33.074, 68.4, 95.63))
    for s in states.states:
        lon.append([])
        lon[j] = s.longitude
        lat.append([])
        lat[j] = s.latitude
        j += 1
    return lon, lat


lon, lat = coordinates()
fig = plt.figure(figsize=(16, 9))
# ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())

# make the map global rather than have it zoom in to
# the extents of any plotted data


ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

for i in range(len(lon)):
    plt.scatter(lon[i], lat[i])

plt.show()
#
# ax.plot(-0.08, 51.53, 'o', transform=ccrs.PlateCarree())
# ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.PlateCarree())
# ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.Geodetic())
# ax.set_global()

# ax.add_feature(cartopy.feature.COASTLINE)
# ax.add_feature(cartopy.feature.OCEAN)
# ax.add_feature(cartopy.feature.BORDERS)
# ax.add_feature(cartopy.feature.LAND)
# ax.gridlines()

plt.show()