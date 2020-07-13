# Geolabels
OpenSource lines for cartographic labeling of physical geographic features

## Brief
The purpose of this repository and data is to start a centralized dataset of lines representing physical features used for labeling in various types of cartographic outputs. As of its creation it consists of approximately 1300 geographic line features covering both land and sea globally. The data primarily represents small scale physical features with the hope of growing it into a dataset useful at all scales. 

The intial data was created from two different sources. 

*   Centerlines from [Natural Earth](https://www.naturalearthdata.com/downloads/10m-physical-vectors/10m-physical-labels/) physical label areas and marine areas using the voronoi diagram based [centerline tool](https://github.com/ungarj/label_centerlines). 
*   Lines extracted from Tom Patterson's new [Physical Map of the Contiguous US](http://www.shadedrelief.com/us-physical/) using MapPublisher. 

## The Data
The data consists of single line features with fields for:
*   name
*   type
*   scalerank
*   minzoom
*   maxzoom
*   date_added
*   date_edited
*   verified

## Contributing
This project is at the ground floor with the hopes that the cartographic community will get involved and expand upon this data for the benefit of all map makers. For now the data exists as one simple geojson file. In time, if involvement increases and the data grows we will explore necessary avenues to improving upon the editing and contribution process.

For now, clone the repository and create a separate branch then edit/add features in whatever GIS editing platform you prefer.

When creating new line features, populate the **name** and **type** fields at a minimum. Other fields, if left blank, will be autopopulated as a pre-commit hook. 

### Type Field

When contributing new features to the data the type field must be populated with one of the following values:

* peninsula
* tundra
* sea
* geoarea
* gulf
* bay
* strait
* channel
* pen_cape
* island_group
* isthmus
* lowland
* plain
* plateau
* wetlands
* valley
* desert
* island
* delta
* coast
* basin
* range_mtn
* foothills
* gorge
* fjord
* sound
* inlet
* lagoon
* river

## Verification
We are relying on checking each other's work for validity and accuracy. There is a **verified** field in the data which will be populated with yes/no if a feature has been verified to exist by another contributor. This way we can edit and assure accuracy and a user of the data can choose if they want to show all or only verified features on their maps. 