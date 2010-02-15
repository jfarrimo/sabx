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

import unittest

from geom import *
from utils import meter_feet

class TestGeomPoint(unittest.TestCase):

    def test_create_blank(self):
        test_pt = Point()
        self.assertEquals(test_pt.lat, 0.0)
        self.assertEquals(test_pt.lon, 0.0)
        self.assertEquals(test_pt.ele, None)
        self.assertEquals(test_pt.usgs, None)
        self.assertEquals(test_pt.id, None)

    def test_create_populated(self):
        test_pt = Point(10.10, 11.11, 100.1, 200.2, '10')
        self.assertEquals(test_pt.lat, 10.10)
        self.assertEquals(test_pt.lon, 11.11)
        self.assertEquals(test_pt.ele, 100.1)
        self.assertEquals(test_pt.usgs, 200.2)
        self.assertEquals(test_pt.id, '10')

    def test_dist_self(self):
        test_pt = Point()
        self.assertEquals(test_pt.calculate_distance(test_pt), 0.0)

class TestGeomLine(unittest.TestCase):

    def setUp(self):
        points = [
            Point(29.738246, -98.103823, 213.6, 206.44480896, '6'),
            Point(29.738285, -98.103958, 213.1, 206.279098511, '7'),
            Point(29.738286, -98.103996, 212.6, 206.126815796, '8'),
            Point(29.738416, -98.10415, 212.1, 205.945068359, '9')
            ]
        self.line = Line(points)

    def test_calc_length(self):
        self.assertAlmostEqual(self.line.calc_length(), 0.023686084161068356)

    def test_find_lowest_highest(self):
        lowest, highest = self.line.find_lowest_highest()
        self.assertEquals(lowest, 212.1 * meter_feet)
        self.assertEquals(highest, 213.6 * meter_feet)

class TestGeomBox(unittest.TestCase):

    def setUp(self):
        self.test_box = Box(10.0, 20.0, 30.0, 40.0)

    def test_create_blank(self):
        blank_box = Box()
        self.assertEquals(blank_box.min_lat, 200.0)
        self.assertEquals(blank_box.min_lon, 200.0)
        self.assertEquals(blank_box.max_lat, -200.0)
        self.assertEquals(blank_box.max_lon, -200.0)

    def test_create_populated(self):
        self.assertEquals(self.test_box.min_lat, 10.0)
        self.assertEquals(self.test_box.min_lon, 20.0)
        self.assertEquals(self.test_box.max_lat, 30.0)
        self.assertEquals(self.test_box.max_lon, 40.0)

    def test_is_pt_in_box_yes(self):
        self.assert_(self.test_box.is_pt_in_box(20.0, 30.0))

    def test_is_pt_in_box_no(self):
        self.assertFalse(self.test_box.is_pt_in_box(5.0, 10.0))

    def test_resize(self):
        self.test_box.resize(1.0, 1.0)
        self.assertAlmostEqual(self.test_box.width(), 1.0, 3)
        self.assertAlmostEqual(self.test_box.height(), 1.0, 3)

    def test_expand_to_point_in(self):
        self.test_box.expand_to_point(20.0, 30.0)
        self.assertEquals(self.test_box.min_lat, 10.0)
        self.assertEquals(self.test_box.min_lon, 20.0)
        self.assertEquals(self.test_box.max_lat, 30.0)
        self.assertEquals(self.test_box.max_lon, 40.0)

    def test_expand_to_point_out(self):
        self.test_box.expand_to_point(5.0, 5.0)
        self.assertEquals(self.test_box.min_lat, 5.0)
        self.assertEquals(self.test_box.min_lon, 5.0)
        self.assertEquals(self.test_box.max_lat, 30.0)
        self.assertEquals(self.test_box.max_lon, 40.0)

    def test_expand_to_box_in(self):
        new_box = Box(11.0, 21.0, 29.0, 39.0)
        self.test_box.expand_to_box(new_box)
        self.assertEquals(self.test_box.min_lat, 10.0)
        self.assertEquals(self.test_box.min_lon, 20.0)
        self.assertEquals(self.test_box.max_lat, 30.0)
        self.assertEquals(self.test_box.max_lon, 40.0)

    def test_expand_to_box_overlap(self):
        new_box = Box(5.0, 15.0, 30.0, 40.0)
        self.test_box.expand_to_box(new_box)
        self.assertEquals(self.test_box.min_lat, 5.0)
        self.assertEquals(self.test_box.min_lon, 15.0)
        self.assertEquals(self.test_box.max_lat, 30.0)
        self.assertEquals(self.test_box.max_lon, 40.0)

    def test_expand_to_box_surround(self):
        new_box = Box(9.0, 19.0, 31.0, 41.0)
        self.test_box.expand_to_box(new_box)
        self.assertEquals(self.test_box.min_lat, 9.0)
        self.assertEquals(self.test_box.min_lon, 19.0)
        self.assertEquals(self.test_box.max_lat, 31.0)
        self.assertEquals(self.test_box.max_lon, 41.0)

if __name__ == "__main__":
    unittest.main()
