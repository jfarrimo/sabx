#! /usr/bin/python
###############################################################################
#
# sabx10.oxm - an SABX file manipulation library
# Copyright (C) 2009, 2010 Jay Farrimond (jay@sabikerides.com)
#
# This file is part of sabx10.oxm.
#
# sabx10.oxm is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# sabx10.oxm is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with sabx10.oxm.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import os
import tempfile
import unittest

import xml.etree.ElementTree as et

from utils import *

class TestUtilsPoints(unittest.TestCase):

    def setUp(self):
        self.lax_lat = 33.0 + (57.0 / 60.0)
        self.lax_lon = -(118.0 + (24.0 / 60.0))

        self.jfk_lat = 40.0 + (38.0 / 60.0)
        self.jfk_lon = -(73.0 + (47.0 / 60.0))

    def test_calculate_distance(self):
        self.assertAlmostEqual(
            calculate_distance(self.lax_lat, self.lax_lon, 
                               self.jfk_lat, self.jfk_lon),
            0.623584645464 * rad_to_nm * nm_to_statute)

    def test_pt_dist_from_pt(self):
        new_pt = pt_dist_from_pt(self.lax_lat, self.lax_lon, 
                                 100.0 * nm_to_statute, 65.8921517923)
        self.assertAlmostEqual(new_pt[0], 34.0 + (37.0 / 60.0), 3)
        self.assertAlmostEqual(new_pt[1], -(116.0 + (33.0 / 60.0)), 2)

    def test_pt_dist_from_pt_up(self):
        new_pt = pt_dist_from_pt(29.738246, -98.103823, 1.0, 0.0)
        self.assertAlmostEqual(new_pt[0], 29.752728937365013)
        self.assertAlmostEqual(new_pt[1], -98.103822999999977)

    def test_pt_dist_from_pt_right(self):
        new_pt = pt_dist_from_pt(29.738246, -98.103823, 1.0, 90.0)
        self.assertAlmostEqual(new_pt[0], 29.738244954303006)
        self.assertAlmostEqual(new_pt[1], -98.087143364652249)

    def test_pt_dist_from_pt_down(self):
        new_pt = pt_dist_from_pt(29.738246, -98.103823, 1.0, 180.0)
        self.assertAlmostEqual(new_pt[0], 29.72376306263499)
        self.assertAlmostEqual(new_pt[1], -98.103822999999977)

    def test_pt_dist_from_pt_left(self):
        new_pt = pt_dist_from_pt(29.738246, -98.103823, 1.0, 270.0)
        self.assertAlmostEqual(new_pt[0], 29.738244954303006)
        self.assertAlmostEqual(new_pt[1], -98.120502635347805)

class TestUtilsXML(unittest.TestCase):

    def setUp(self):
        sabx_valid = """<?xml version='1.0' encoding='utf-8'?>
<rideset xmlns="http://www.sabikerides.com/SABX/1/0/"
	 version="1.0">

  <uuid>147dbb84-d109-44f7-9ac2-09b2a736993f</uuid>
  <version>1</version>
  <zip_prefix>781</zip_prefix>

  <ride_type>road</ride_type>
  <title>Tour de Gruene 2009 Tour</title>
  <description><p>This is the tour route for the 2009 Tour de Gruene.  
      The time trial courses will have their own map.
      Please note that the stops listed on this map are not the official
      rest areas for the ride.  Those will come later.  For now I have 
      included the stops you would use if you did the ride on your own.</p>
    <p>Check out the <a href="http://www.tourdegruene.com/">Tour de Gruene 
	web site</a> for more information.</p>
  </description>
  <terrain>Flat</terrain>

  <segment id='2'>
    <road>Gruene Rd.</road>
    <fromto>parking to Hunter Rd.</fromto>
    <comments>Gruene Hall is on your left.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Moderate</traffic>
    <speed>20</speed>
    <waypoint id='6'>
      <lat>29.738246</lat>
      <lon>-98.103823</lon>
      <ele>213.6</ele>
      <usgs>206.44480896</usgs>
    </waypoint>
    <waypoint id='7'>
      <lat>29.738285</lat>
      <lon>-98.103958</lon>
      <ele>213.1</ele>
      <usgs>206.279098511</usgs>
    </waypoint>
    <waypoint id='8'>
      <lat>29.738286</lat>
      <lon>-98.103996</lon>
      <ele>212.6</ele>
      <usgs>206.126815796</usgs>
    </waypoint>
    <waypoint id='9' stop='0a'>
      <lat>29.738416</lat>
      <lon>-98.10415</lon>
      <ele>212.6</ele>
      <usgs>205.945068359</usgs>
    </waypoint>
  </segment>
</rideset>"""

        sabx_invalid_version = """<?xml version='1.0' encoding='utf-8'?>
<rideset xmlns="http://www.sabikerides.com/SABX/1/0/"
	 version="2.0">
  <uuid>147dbb84-d109-44f7-9ac2-09b2a736993f</uuid>
</rideset>"""

        self.file_valid = tempfile.TemporaryFile(mode='w+')
        self.file_valid.write(sabx_valid)
        self.file_valid.seek(0, os.SEEK_SET)

        self.file_invalid_version = tempfile.TemporaryFile(mode='w+')
        self.file_invalid_version.write(sabx_invalid_version)
        self.file_invalid_version.seek(0, os.SEEK_SET)

    def test_check_version_valid(self):
        tree = parse_no_def_namespaces(self.file_valid)
        self.assert_(check_version(tree))

    def test_check_version_invalid(self):
        tree = parse_no_def_namespaces(self.file_invalid_version)
        self.assertRaises(VersionException, check_version, tree)

    def test_get_from_id_found(self):
        tree = parse_no_def_namespaces(self.file_valid)
        pts = tree.findall("segment/waypoint")
        self.assert_(get_from_id(pts, '7'))

    def test_get_from_id_not_found(self):
        tree = parse_no_def_namespaces(self.file_valid)
        pts = tree.findall("segment/waypoint")
        self.assertFalse(get_from_id(pts, '77'))

    def test_parse_no_def_namespaces_yes_namespace(self):
        full_tree = et.parse(self.file_valid)
        self.file_valid.seek(0, os.SEEK_SET)
        no_namespace_tree = parse_no_def_namespaces(self.file_valid)

        self.assert_(
            full_tree.findtext(
                '{http://www.sabikerides.com/SABX/1/0/}title'))
        self.assertFalse(
            no_namespace_tree.findtext(
                '{http://www.sabikerides.com/SABX/1/0/}title'))

    def test_parse_no_def_namespaces_no_namespace(self):
        full_tree = et.parse(self.file_valid)
        self.file_valid.seek(0, os.SEEK_SET)
        no_namespace_tree = parse_no_def_namespaces(self.file_valid)

        self.assertFalse(full_tree.findtext('title'))
        self.assert_(no_namespace_tree.findtext('title'))
    
if __name__ == "__main__":
    unittest.main()
