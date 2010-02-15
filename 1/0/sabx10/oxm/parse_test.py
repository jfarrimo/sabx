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

from utils import parse_no_def_namespaces

from parse_test_data import test_data
from parse import *

class TestParse(unittest.TestCase):

    def setUp(self):
        file_valid = tempfile.TemporaryFile(mode='w+')
        file_valid.write(test_data)
        file_valid.seek(0, os.SEEK_SET)
        self.tree = parse_no_def_namespaces(file_valid)

    def test_parse_tree(self):
        sabx = parse_tree(self.tree)

        # top level
        self.assertEquals(sabx['uuid'], "147dbb84-d109-44f7-9ac2-09b2a736993f")
        self.assertEquals(sabx['version'], "1")
        self.assertEquals(sabx['zip_prefix'], "781")
        self.assertEquals(sabx['ride_type'], "road")
        self.assertEquals(sabx['title'], "Tour de Gruene 2009 Tour")
        self.assertEquals(sabx['description'][:20], "<p>This is the tour ")
        self.assertEquals(sabx['terrain'], "Flat")

        # history
        self.assertEquals(len(sabx['history']), 3)
        self.assertEquals(sabx['history'][0].version, '1')
        self.assertEquals(sabx['history'][0].date, '2009-06-03')
        self.assertEquals(sabx['history'][0].description, 
                          'Created short loop east of town.')

        # photos
        self.assertEquals(sabx['photos'].title, 'Returning via River Rd.')
        self.assertEquals(
            sabx['photos'].src, 
            'http://farm4.static.flickr.com/3352/3639773356_2435f78398_m.jpg')
        self.assertEquals(len(sabx['photos'].photo_list), 1)
        self.assertEquals(sabx['photos'].photo_list[0].desc, 
                          '2009-06-07 Gruene')
        self.assertEquals(
            sabx['photos'].photo_list[0].href, 
            'http://www.flickr.com/photos/sabikerides/sets/72157619945875214/')

        # parking
        self.assertEquals(len(sabx['park_list']), 1)
        self.assertEquals(sabx['park_list'][0].id, '1')
        self.assertEquals(sabx['park_list'][0].description[:20], 
                          'Gruene has plenty of')
        self.assertEquals(sabx['park_list'][0].lat, 29.737931)
        self.assertEquals(sabx['park_list'][0].lon, -98.103585)

        # turns
        self.assertEquals(len(sabx['turn_list']), 53)
        self.assertEquals(sabx['turn_list'][0].id, '1')
        self.assertEquals(sabx['turn_list'][0].fromto, 'parking to Hunter Rd.')
        self.assertEquals(sabx['turn_list'][0].cue, 'RIGHT onto Gruene Rd.')
        self.assertEquals(
            sabx['turn_list'][0].comments, 
            'From the parking lot, turn right onto Gruene Rd.')

        # segments
        self.assertEquals(len(sabx['seg_list']), 53)
        self.assertEquals(sabx['seg_list'][0].id, '2')
        self.assertEquals(sabx['seg_list'][0].road, 'Gruene Rd.')
        self.assertEquals(sabx['seg_list'][0].fromto, 'parking to Hunter Rd.')
        self.assertEquals(
            sabx['seg_list'][0].comments, 
            'Gruene Hall is on your left.')
        self.assertEquals(sabx['seg_list'][0].lanes, '2')
        self.assertEquals(sabx['seg_list'][0].shoulder, '0')
        self.assertEquals(sabx['seg_list'][0].traffic, 'Moderate')
        self.assertEquals(sabx['seg_list'][0].speed, '20')

        # waypoints
        self.assertEquals(len(sabx['seg_list'][0].waypoints), 4)
        self.assertEquals(sabx['seg_list'][0].waypoints[0].id, '6')
        self.assertEquals(sabx['seg_list'][0].waypoints[0].lat, 29.738246)
        self.assertEquals(sabx['seg_list'][0].waypoints[0].lon, -98.103823)
        self.assertEquals(sabx['seg_list'][0].waypoints[0].ele, 213.6)
        self.assertEquals(sabx['seg_list'][0].waypoints[0].usgs, 206.44480896)

        # stops
        self.assertEquals(len(sabx['stop_list']), 13)
        self.assertEquals(sabx['stop_list'][0].id, '0a')
        self.assertEquals(sabx['stop_list'][0].type, 'conv. store')
        self.assertEquals(sabx['stop_list'][0].description[:20], 
                          'There are many bars ')
        self.assertEquals(sabx['stop_list'][0].lat, 29.738416)
        self.assertEquals(sabx['stop_list'][0].lon, -98.10415)

        # pois
        self.assertEquals(len(sabx['poi_list']), 7)
        self.assertEquals(sabx['poi_list'][0].id, '1')
        self.assertEquals(sabx['poi_list'][0].description[:20], 
                          'The local land-fill ')
        self.assertEquals(sabx['poi_list'][0].lat, 29.742733333)
        self.assertEquals(sabx['poi_list'][0].lon, -98.0301)

        # rides
        self.assertEquals(len(sabx['ride_list']), 4)
        self.assertEquals(sabx['ride_list'][0].id, '1')
        self.assertEquals(sabx['ride_list'][0].description[:20], 
                          'The short loop takes')
        self.assertEquals(sabx['ride_list'][0].parking, '1')
        self.assertEquals(len(sabx['ride_list'][0].turns), 18)
        self.assertEquals(sabx['ride_list'][0].turns[0], '1')
        self.assertEquals(len(sabx['ride_list'][0].segs), 18)
        self.assertEquals(sabx['ride_list'][0].segs[0], '2')

    def test_process_ride(self):
        pass

if __name__ == "__main__":
    unittest.main()
