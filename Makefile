new_geolabels.geojson:
	# convert original sqlite to geojson
	ogr2ogr -f Geojson -t_srs EPSG:3857 -nln geolabels data/___original_geolabels.geojson data/___original_geolabels.sqlite
	# merge all geojsons in the new_data directory
	ogrmerge.py -t_srs EPSG:3857 -f GeoJSON -nln geolabels -o geolabels/new_geolabels.geojson data/*.geojson -single -field_strategy FirstLayer -progress -overwrite_ds

geolabels: new_geolabels.geojson
	# populate empty fields and create a new master file
	python3 populate_fields.py
	ogr2ogr -f SQLite -progress -dsco SPATIALITE=YES -dim XY -nln geolabels geolabels/geolabels.sqlite geolabels/geolabels.geojson
	# cleanup processing
	rm data/___original_geolabels.geojson
	mv data/*.geojson data/archived
	cp -r geolabels/new_geolabels.geojson data/___original_geolabels.geojson
	ogr2ogr -f SQLite -progress -dsco SPATIALITE=YES -dim XY -nln geolabels data/___original_geolabels.sqlite data/___original_geolabels.geojson
	rm -rf data/___original_geolabels.geojson
	rm -rf geolabels/new_geolabels.geojson
	rm -rf geolabels/geolabels.geojson