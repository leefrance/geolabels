# Geolabels
OpenSource lines for cartographic labeling of physical geographic features

## Brief
The purpose of this repository and data is to start a centralized dataset of lines representing physical features used for labeling in various types of cartographic outputs. As of its creation it consists of approximately 1300 geographic line features covering both land and sea globally. The data primarily represents small scale physical features with more detail in the contiguous USA thanks to Tom Patterson's map. The goal is to grow the extent and detail of the lines so they are useful at all scales. 

The intial data was created from two different sources. 

*   Centerlines from [Natural Earth](https://www.naturalearthdata.com/downloads/10m-physical-vectors/10m-physical-labels/) physical label areas and marine areas using the voronoi diagram based [centerline tool](https://github.com/ungarj/label_centerlines). 
*   Lines extracted from Tom Patterson's new [Physical Map of the Contiguous US](http://www.shadedrelief.com/us-physical/) using MapPublisher. 

## The Data
`geolabels/geolabels.geojson` represents the current polished version of the geolabels data and is the one you should use for incorporation into your projects. The other data in `data/` contains new data contributions and the file that should be edited when making corrections to the existing data. Follow the instructions below for contributing and editing.

The data consists of single line features with fields for:
*   name
*   type
*   scalerank
*   minzoom
*   maxzoom
*   date_added
*   date_edited
*   verified

### Type Field
All features currently exist as one of the following types:

* basin
* bay
* canyon
* channel
* coast
* delta
* desert
* fjord
* foothills
* geoarea
* gorge
* gulch
* gulf
* inlet
* island
* island_group
* isthmus
* lagoon
* lowland
* pen_cape
* peninsula
* plain
* plateau
* range_mtn
* ridge
* river
* sea
* sound
* strait
* tundra
* valley
* wetlands

### Scalerank
Natural Earth derived ranking number from 0 to 9. Lower numbers being of greater significance on the map, higher numbers being smaller and less prominent features.

### Min and Max Zoom
If using the data for vector or raster tiles the min and max zoom fields help determine when during the zoom a feature should appear on the map.

### Dates added and edited
Date added is the date that the feature was initially added to the data. Date edited will be populated if someone makes changes to a feature.

### Verified
Yes or null values if the feature has been verified for accuracy and validity by another user.

## Contributing
This project is at the ground floor with the hopes that the cartographic community will get involved and expand upon this data for the benefit of all map makers. For now the data exists as a simple geojson file. In time, if involvement increases and the data grows we will explore necessary avenues to improving upon the editing and contribution process.

**Adding Features**
It's important that if you are creating new features that you **create a separate geojson of only your new features** with the same field schema of the original data. This is my workflow, but feel free to come up with your own:
* Clone the repository and create a separate branch 
* Open `data/___original_geolabels.geojson` in QGIS and start editing and add your new line features.
* Without saving the edits, export your new features to a separate geojson file. Try to model the name of your new file based on what you see in the `/data/archive` folder
* Stop editing and don't save edits (we want to preserve what's in the original geolabels geojson)

When creating new line features, populate the **name** and **type** fields at a minimum. When contributing new features to the data the type field must be populated with one of the existing values listed above. Other fields, if left blank, will be autopopulated later.

After your pull request has been reviewed and merged one of the codeowners will run the process for updating the master geolabels file in `geolabels/geolabels.geojson`and then your contributed geojson will be moved to the archive. 

**Editing Features**
If you want to correct errors you've found in the data, verify new features, adjust the alignment of something, ect, follow the same steps above but just edit the `data/___original_geolabels.geojson`, as long as you aren't creating new features. I think merge conflicts should be less of an issue with editing if multiple people are working on it at the same time. I'm hoping to improve upon this process later on

**Merge Conflicts**
If merge conflicts arise when editing `data/___original_geolabels.geojson` you can resolve conflicts by performing a git pull on master into your branch, and opening the conflicting file in a program like VS Code. Scroll to the area of conflict and _accept both changes_. Then use something like [Mapbox geojsonhint](https://github.com/mapbox/geojsonhint) to pinpoint where exactly in the geojson syntax errors might have occurred, as I have yet to find a VS Code linter for geojson files. **This step is important to making sure the edited geojson is valid before pushing changes**.

## Verification
We are relying on checking each other's work for validity and accuracy. There is a **verified** field in the data which will be populated with `yes` if a feature has been verified to exist by another contributor. This way we can edit and assure accuracy and a user of the data can choose if they want to show all or only verified features on their maps. If you want to help verify new features clone the repo and view/edit in your favorite GIS program and add `yes` to any new features you verify for accuracy. If you discover errors you may correct them and then update the **date_edited** field as well.

## Data to Add
If you don't want to go through the process of adding line features to the geolabels.geojson but have some good line or polygon data you'd like to see added as more geolabels, please include a link to it here as long as the data is free to use.

## Codeowners
If you would like to become a code owner and help with reviewing pull requests and managing the repo please let me know!
