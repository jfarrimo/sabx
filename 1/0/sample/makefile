#-*-Makefile-*-
################################################################################
#
# Assume the following directory structure.  All directory names end in 
# slash ('/'). Everything under the temp directory will be created by the 
# make file.
#
# makefile
# ride_data/
#   sample_ride/
#     sample.sabx
# site/
#   markers/
#   images/
#   css/
#   js/
#   rides/
#   staging/
# temp/
#   sample_ride/
#     osm/
#     profile/
#     print/
#
# Setting makefile variables:
#
# map_template_dir - the map templates are installed as part of the sabx_map
# package and are in a templates sub-directory of its package directory
#
# map_web_dir - the map css & js files are installed as part of the sabx_osm
# package and are possibly in the directory 
# /usr/local/share/applications/sabx/map_web
#
# osm_template_dir - the osm templates are installed as part of the sabx_osm
# package and are in a templates sub-directory of its package directory
#
# osm_image_dir - the osm images are installed as part of the sabx_osm
# package and are possibly in the directory 
# /usr/local/share/applications/sabx/osm_images
#
# BTW, the convention here is no ending slashes in path variables.
#
################################################################################

mapset: site/css/ride.css \
site/js/ride.js \
site/rides/sample.html \
site/rides/sample.js \
temp/sample_ride/osm \
temp/sample_ride/osm/render.py \
temp/sample_ride/osm/map.osm \
temp/sample_ride/osm/styles_0.xml \
temp/sample_ride/osm/styles_cluster_0.xml \
temp/sample_ride/osm/sample_map_0.png \
temp/sample_ride/profile \
site/rides/sample_prof_large_0_all.png \
temp/sample_ride/profile/sample_prof_large_0_all.png \
temp/sample_ride/profile/sample_prof_0.pdf \
temp/sample_ride/print \
temp/sample_ride/print/sample_0.pdf \
site/rides/sample_0.pdf
.PHONY: mapset

staging: site/staging/sample.html site/staging/sample.js
.PHONY: staging

map_template_dir = /usr/local/lib/python2.6/dist-packages/sabx10/map/templates
osm_template_dir = /usr/local/lib/python2.6/dist-packages/sabx10/osm/templates

# RIDE
site/rides/sample.html: ride_data/sample_ride/sample.sabx \
$(map_template_dir)/ride_template.jinja2
	sabx_map_ride -i $< -o $@ -r "../markers" -g "../images" -c "../css" -j "../js" -b ".."

site/rides/sample.js: ride_data/sample_ride/sample.sabx \
$(map_template_dir)/ridedata_template.jinja2
	sabx_map_ridedata -i $< -o $@

# OSM
temp/sample_ride/osm:
	mkdir -p $@

temp/sample_ride/osm/render.py: ride_data/sample_ride/sample.sabx \
$(osm_template_dir)/render_template.jinja2
	sabx_osm_render -i $< -o $@
	chmod 755 $@

temp/sample_ride/osm/map.osm: ride_data/sample_ride/sample.sabx \
$(osm_template_dir)/osm_template.jinja2
	sabx_osm_osm -i $< -o $@

temp/sample_ride/osm/styles_0.xml: ride_data/sample_ride/sample.sabx \
$(osm_template_dir)/styles_template.jinja2
	sabx_osm_styles -i $< -o $(subst _0.xml,,$@) -l ~/sabx/site/images

temp/sample_ride/osm/styles_cluster_0.xml: ride_data/sample_ride/sample.sabx \
$(osm_template_dir)/styles_cluster_template.jinja2
	sabx_osm_styles_cluster  -i $< -o $(subst _0.xml,,$@) -l ~/sabx/site/images

temp/sample_ride/osm/sample_map_0.png: ride_data/sample_ride/sample.sabx \
temp/sample_ride/osm/render.py
	temp/sample_ride/osm/render.py ~/sabx/temp/sample_ride/osm/styles ~/sabx/temp/sample_ride/osm/sample_map

# PROFILE
temp/sample_ride/profile:
	mkdir -p $@

site/rides/sample_prof_large_0_all.png: ride_data/sample_ride/sample.sabx
	sabx_profiles_plot -s -i $< ~/sabx/site/rides/sample

temp/sample_ride/profile/sample_prof_large_0_all.png: ride_data/sample_ride/sample.sabx
	sabx_profiles_plot -r -i $< ~/sabx/temp/sample_ride/profile/sample

temp/sample_ride/profile/sample_prof_0.pdf: ride_data/sample_ride/sample.sabx \
temp/sample_ride/profile/sample_prof_large_0_all.png
	sabx_profiles2pdf -i $< ~/sabx/temp/sample_ride/profile/sample ~/sabx/temp/sample_ride/profile/sample

# PDF
temp/sample_ride/print:
	mkdir -p $@

temp/sample_ride/print/sample_0.pdf: ride_data/sample_ride/sample.sabx
	sabx_pdf_instructions -i $< ~/sabx/temp/sample_ride/print/sample

site/rides/sample_0.pdf: \
ride_data/sample_ride/sample.sabx \
temp/sample_ride/osm/sample_map_0.png \
temp/sample_ride/print/sample_0.pdf \
temp/sample_ride/profile/sample_prof_0.pdf
	sabx_pdf_combine -i ~/sabx/ride_data/sample_ride/sample.sabx \
site/rides/sample_0.pdf \
temp/sample_ride/osm/sample_map_0.pdf \
temp/sample_ride/print/sample_0.pdf \
temp/sample_ride/profile/sample_prof_0.pdf

# STAGING
site/staging/sample.html: ride_data/sample_ride/sample.sabx
	sabx_map_staging -i $< -o $@ -r "../markers" -g "../images" -c "../css" -j "../js" -b ".."

site/staging/sample.js: ride_data/sample_ride/sample.sabx
	sabx_map_ridedata -i $< -o $@
