#!/usr/bin/python
###############################################################################
#
# sabx10 - an SABX file manipulation library
# Copyright (C) 2009, 2010 Jay Farrimond (jay@sabikerides.com)
#
# This file is part of sabx10.
#
# sabx10 is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# sabx10 is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# sabx10.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from distutils.core import setup

setup(name='sabx10',
      version='1.1',
      description='SABX file handling',
      long_description='Create and manipulate SABX files',
      license='GPLv3+, LGPLv3+',
      author='Jay Farrimond',
      author_email='jay@sabikerides.com',
      url='http://www.sabikerides.com/sabx/1/0/sabx10.html',
      packages=['sabx10', 'sabx10.map', 'sabx10.osm', 'sabx10.oxm', 
                'sabx10.pdf_gen', 'sabx10.profiles', 'sabx10.templating', 
                'sabx10.utils'],
      package_data={'sabx10.utils': ['templates/*.jinja2'],
                    'sabx10.map': ['templates/*.jinja2'], 
                    'sabx10.osm': ['templates/*.jinja2']}, 
      scripts=['sabx10/gpx2sabx', 'sabx10/sabx2csv', 'sabx10/sabx2html', 
               'sabx10/sabx_cleanup', 'sabx10/sabx_csv', 
               'sabx10/sabx_ele_analyze', 'sabx10/sabx_number', 
               'sabx10/sabx_pretty', 'sabx10/sabx_seg_closest', 
               'sabx10/sabx_seg_reverse', 'sabx10/sabx_usgs', 
               'sabx10/tcx2sabx', 'sabx10/template_to', 
               'sabx10/sabx_map_ride', 'sabx10/sabx_map_ridedata', 
               'sabx10/sabx_map_staging', 'sabx10/sabx_osm_osm', 
               'sabx10/sabx_osm_render', 'sabx10/sabx_osm_styles', 
               'sabx10/sabx_osm_styles_cluster', 'sabx10/sabx_pdf_combine', 
               'sabx10/sabx_pdf_instructions', 'sabx10/sabx_profiles2pdf', 
               'sabx10/sabx_profiles_plot'],
     )
