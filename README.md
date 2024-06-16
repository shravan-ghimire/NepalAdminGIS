# NepalAdminGIS

This repository contains the administrative boundary of Nepal from the perspective of the Government of Nepal and the Nepali people. The presented data and maps are based on Nepal's new map, which was approved by the parliament and ratified by the president in 2020. This repository aims to offer information about the administrative geospatial data in Nepal and its footprint in the world. It is expected that users and enthusiasts will be able to map Nepal's global footprint accurately without requiring additional processing and GIS skills.

Nepal has 5 administrative levels from Level 0 (country boundary) to Level 4 (municipality ward boundary). The data other than Level 4 can be accessed freely from the Department of Survey (DoS) on [webs](https://nationalgeoportal.gov.np/#/metadata/97 under free use license with restriction to redistribute or resale the data to the third party. The use limitation information can be assessed from the provided web link.
![Nepal_adminsitrative_levels](https://github.com/shravan-ghimire/NepalAdminGIS/assets/83561429/3067adb3-0c4f-4756-9603-605cef39cb4f)

The NepalAdminGIS file shared here contains the Level 0 to Level 3 boundaries and Python code to plot on a Python environment. It is reiterated that the license of these esri shapefiles belongs to the Department of Survey Nepal not to the author of this repository. 
Map of Level 0 and Level 1 as per the provided Python code is as follows;
![Nepal_boundary](https://github.com/shravan-ghimire/NepalAdminGIS/assets/83561429/c53a113b-1e53-4625-b824-4ba26fc9cf2c)

The maps of Level 2 and Level 3 boundaries are shown below, also generated using the provided Python code;
![Nepal_local_level](https://github.com/shravan-ghimire/NepalAdminGIS/assets/83561429/d02c1128-980d-42dc-87ba-f42247a32946)

Here the official boundary of Nepal is incorporated into the GADM administrative boundary of the world. GADM boundaries are freely available for academic and non-profit use from: https://gadm.org/download_world.html . The following method is used to integrate Nepal's official boundary into the world country dataset.
![GADM_Editing_Procedure](https://github.com/shravan-ghimire/NepalAdminGIS/assets/83561429/b1b3522b-d681-4bbc-a4cc-2978b6ac0e26)

The resultant map of the world is shown below;
![Figure_Nepal_in_GADM](https://github.com/shravan-ghimire/NepalAdminGIS/assets/83561429/f7a6ec53-480a-4089-a82d-615e89a0d28d)
![Figure_Nepal_in_GADM_Zoomed_out](https://github.com/shravan-ghimire/NepalAdminGIS/assets/83561429/6dddb6a7-45fb-4175-bafd-0be103b98a60)


The world countries data can be downloaded from here: https://archive.org/details/nepal-world-standard-shapefiles-master
