#libraries required
import geopandas as gpd
import matplotlib.pyplot as plt

#loading data
gdf0 = gpd.read_file('NepalAdminGIS/nepal-standard-shapefiles-master/shapefiles/nepal_bnd_wgs84.shp') #national boundary, level 0
gdf1 = gpd.read_file('NepalAdminGIS/nepal-standard-shapefiles-master/shapefiles/nepal_province_wgs84.shp') #provincial boundry, level 1

# plot the data
fig, ax = plt.subplots(figsize=(10,8))
gdf0.plot(ax=ax, color='white', edgecolor='red', linewidth=1.5)
gdf1.plot(ax=ax, color='white', edgecolor='black', linewidth=0.5)

# label the features, labels are in 'Province' column
for idx, row in gdf1.iterrows():
    plt.annotate(text=row['Province'], xy=(row.geometry.centroid.x, row.geometry.centroid.y),
                 xytext=(3, 3), textcoords="offset points", fontsize=8, fontweight='bold', color='black')

ax.set_title("Nepal Boundary")
ax.grid(True, color='grey', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.savefig('NepalAdminGIS/Nepal_boundary.png', dpi=500)
#plt.show()