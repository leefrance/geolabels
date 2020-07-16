new_geolabels.geojson:
	# merge all geojsons in the new_data directory
	ogrmerge.py -t_srs EPSG:3857 -f GeoJSON -nln geolabels -o geolabels/new_geolabels.geojson data/*.geojson -single -field_strategy FirstLayer -progress -overwrite_ds

geolabels: new_geolabels.geojson
	# populate empty fields and create a new master file
	python3 populate_fields.py
	cp -r geolabels/new_geolabels.geojson data/___original_geolabels.geojson
	rm -rf geolabels/new_geolabels.geojson