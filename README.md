# NepalAdminGIS

This repository contains the administrative boundary of Nepal from the perspective of the Government of Nepal and the Nepali people. The presented data and maps are based on Nepal's new map, which was approved by the parliament and ratified by the president in 2020. This repository aims to offer information about the administrative geospatial data in Nepal and its footprint in the world. It is expected that users and enthusiasts will be able to map Nepal's global footprint accurately without requiring additional processing and GIS skills.

Nepal has 5 administrative levels from Level 0 (country boundary) to Level 4 (municipality ward boundary). The data other than Level 4 can be accessed freely from the Department of Survey (DoS) on [webs](https://nationalgeoportal.gov.np/#/metadata/97 under free use license with restriction to redistribute or resale the data to the third party. The use limitation information can be assessed from the provided web link.
![Nepal_adminsitrative_levels](https://github.com/shravanghimire93/NepalAdminGIS/assets/83561429/e96b6e0d-9461-4eb0-ae77-a8fd6ad2a512)

The NepalAdminGIS file shared here contains the Level 0 to Level 3 boundaries and Python code to plot on a Python environment. It is reiterated that the license of these esri shapefiles belongs to the Department of Survey Nepal not to the author of this repository. 
Map of Level 0 and Level 1 as per the provided Python code is as follows;
![Nepal_boundary](https://github.com/shravanghimire93/NepalAdminGIS/assets/83561429/84fd679d-4438-4411-8836-b72dabd2391e)

The maps of Level 2 and Level 3 boundaries are shown below, also generated using the provided Python code;
![Nepal_local_level](https://github.com/shravanghimire93/NepalAdminGIS/assets/83561429/b2a1e6a5-00ec-458f-84f3-6a56ab79b596)

Here the official boundary of Nepal is incorporated into the GADM administrative boundary of the world. GADM boundaries are freely available for academic and non-profit use from: https://gadm.org/download_world.html . The following method is used to integrate Nepal's official boundary into the world country dataset.
![GADM_Editing_Procedure](https://github.com/shravanghimire93/NepalAdminGIS/assets/83561429/79192bde-59d9-43a8-b029-f45885da89c7)

The resultant map of the world is shown below;
![Figure_Nepal_in_GADM](https://github.com/shravanghimire93/NepalAdminGIS/assets/83561429/85a93808-8b04-4cbf-9002-3a51cd9686b6)
![Figure_Nepal_in_GADM_Zoomed_out](https://github.com/shravanghimire93/NepalAdminGIS/assets/83561429/4f20882e-aade-49e9-8fd8-2ceec9d518d7)

The world countries data can be downloaded from here: https://archive.org/details/nepal-world-standard-shapefiles-master
