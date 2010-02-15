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
from ride import *

class TestProcess(unittest.TestCase):

    def setUp(self):
        file_valid = tempfile.TemporaryFile(mode='w+')
        file_valid.write(test_data)
        file_valid.seek(0, os.SEEK_SET)
        self.tree = parse_no_def_namespaces(file_valid)

    def test_process_rides(self):
        rides, bounds = process_rides(self.tree)

        self.assertEquals(len(rides), 4)
        self.assertEquals(len(rides[0].turns), 18)
        self.assertEquals(len(rides[0].segs), 18)
        self.assertEquals(len(rides[0].pois), 1)
        self.assertEquals(len(rides[0].stops), 5)
        self.assertEquals(rides[0].index, 0)

if __name__ == "__main__":
    unittest.main()
