#!/usr/bin/env python3
import json
from shapely.geometry import shape
import datetime

input_file = "working_dataset/geolabels.geojson"
output_file = "master_dataset/geolabels_master.geojson"
date_object = datetime.date.today()

with open(input_file) as data:
    geojson = json.load(data)
    features = geojson.get('features')
    for line in features:
        length = shape(line['geometry']).length
        scalerank = line['properties']['scalerank']
        minzoom = line['properties']['minzoom']
        maxzoom = line['properties']['maxzoom']
        date_added = line['properties']['date_added']
        name = line['properties']['name']
        if length >= 2000000 and scalerank == None and str.isupper(name) == True:
            line['properties']['scalerank'] = 0
            line['properties']['minzoom'] = 2
            line['properties']['maxzoom'] = 6
        if length >= 2000000 and scalerank == None and str.isupper(name) == False:
            line['properties']['scalerank'] = 1
            line['properties']['minzoom'] = 2
            line['properties']['maxzoom'] = 6
        if length < 2000000 and length >= 1000000 and scalerank == None and str.isupper(name) == True:
            line['properties']['scalerank'] = 1
            line['properties']['minzoom'] = 2
            line['properties']['maxzoom'] = 6
        if length < 2000000 and length >= 1000000 and scalerank == None and str.isupper(name) == False:
            line['properties']['scalerank'] = 2
            line['properties']['minzoom'] = 2
            line['properties']['maxzoom'] = 6
        if length < 1000000 and length >= 500000 and scalerank == None and str.isupper(name) == True:
            line['properties']['scalerank'] = 3
            line['properties']['minzoom'] = 4
            line['properties']['maxzoom'] = 8
        if length < 1000000 and length >= 500000 and scalerank == None and str.isupper(name) == False:
            line['properties']['scalerank'] = 4
            line['properties']['minzoom'] = 5
            line['properties']['maxzoom'] = 9
        if length < 500000 and length >= 100000 and scalerank == None and str.isupper(name) == True:
            line['properties']['scalerank'] = 5
            line['properties']['minzoom'] = 7
            line['properties']['maxzoom'] = 10
        if length < 500000 and length >= 100000 and scalerank == None and str.isupper(name) == False:
            line['properties']['scalerank'] = 5
            line['properties']['minzoom'] = 7
            line['properties']['maxzoom'] = 10
        if length < 100000 and length >= 60000 and scalerank == None and str.isupper(name) == True:
            line['properties']['scalerank'] = 6
            line['properties']['minzoom'] = 8
            line['properties']['maxzoom'] = 11
        if length < 100000 and length >= 60000 and scalerank == None and str.isupper(name) == False:
            line['properties']['scalerank'] = 6
            line['properties']['minzoom'] = 8
            line['properties']['maxzoom'] = 11
        if length < 60000 and length >= 10000 and scalerank == None and str.isupper(name) == True:
            line['properties']['scalerank'] = 7
            line['properties']['minzoom'] = 9
            line['properties']['maxzoom'] = 12
        if length < 60000 and length >= 10000 and scalerank == None and str.isupper(name) == False:
            line['properties']['scalerank'] = 8
            line['properties']['minzoom'] = 9
            line['properties']['maxzoom'] = 12
        if length < 10000 and scalerank == None and str.isupper(name) == True:
            line['properties']['scalerank'] = 8
            line['properties']['minzoom'] = 11
            line['properties']['maxzoom'] = 14
        if length < 10000 and scalerank == None and str.isupper(name) == False:
            line['properties']['scalerank'] = 9
            line['properties']['minzoom'] = 11
            line['properties']['maxzoom'] = 14
        if date_added == None:
            line['properties']['date_added'] = str(date_object)

with open (output_file, 'w+') as f:
    json.dump(geojson, f)