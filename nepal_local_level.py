#libraries required
import geopandas as gpd
import matplotlib.pyplot as plt

#loading data
gdf2 = gpd.read_file('NepalAdminGIS/nepal-standard-shapefiles-master/shapefiles/nepal_districts_wgs84.shp') #district boundary, level 2
gdf3 = gpd.read_file('NepalAdminGIS/nepal-standard-shapefiles-master/shapefiles/nepal_gapanapa_wgs84.shp') #municipal boundry, level 3

#plot the data
fig, ax=plt.subplots(figsize=(10,8))
gdf3.plot(ax=ax, color='silver', edgecolor='white', linewidth=0.5)
gdf2.plot(ax=ax, facecolor='none', edgecolor='maroon', linewidth=0.5)

# label the features, labels are in 'FIRST_DIST' column
for idx, row in gdf2.iterrows():
    plt.annotate(text=row['FIRST_DIST'], xy=(row.geometry.centroid.x, row.geometry.centroid.y),
                 xytext=(3, 3), textcoords="offset points", fontsize=4, fontweight='bold', color='black')

ax.set_title("Nepal Local Level Boundary")
ax.grid(True, color='grey', linestyle='--', linewidth=0.5)


plt.tight_layout()
plt.savefig('NepalAdminGIS/Nepal_local_level.png', dpi=500)
#plt.show()
