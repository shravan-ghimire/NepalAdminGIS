#libraries required
import geopandas as gpd
import matplotlib.pyplot as plt

#loading data
gdf_global = gpd.read_file('NepalAdminGIS/nepal-world-standard-shapefiles-master/shapefiles/gadm_world_map_np.shp')
gdf_nepal = gdf_global[gdf_global['NAME_0']=='Nepal']

#plot the data
fig, ax=plt.subplots(figsize=(10,8))
gdf_global.plot(ax=ax, color='lightgrey', edgecolor='white', linewidth=0.2)
gdf_nepal.plot(ax=ax, facecolor='none', edgecolor='red', linewidth=0.5)
ax.set_title('Nepal in GADM Data')

plt.tight_layout()
plt.savefig('NepalAdminGIS/Figure_Nepal_in_GADM.png', dpi=500)
#plt.show()