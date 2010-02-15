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
"""
Handle renumbering the ids in an SABX file.
"""

from sabx10.templating import SabxProcessor

class Id(object):
    """
    Keep track of the ids for the NumProcessor class.

    @ivar unique: unique ids?
    @type ivar: C{boolean}
    @ivar start_val: starting id value
    @type start_val: C{int}
    @ivar val: current id value
    @type val: C{int}
    """
    def __init__(self, start_val=0, unique=False):
        """
        Setup the instance variables.
        """
        self.unique = unique
        self.start_val = self.val = start_val

    def reset(self):
        """
        Start over counting.
        """
        if not self.unique:
            self.val = self.start_val

    def next(self):
        """
        Get the next id.
        """
        ret_val = self.val
        self.val += 1
        return str(ret_val)

    def range(self, length):
        """
        Get a list of ids.
        """
        self.reset()
        start = self.val
        self.val += length
        return [str(index) for index in range(start, self.val)]

class NumProcessor(SabxProcessor):
    """
    Sequentially renumber the ids of all the items in the SABX 1.0 file.  This
    includes parking places, stops, pois, segments, turns, and rides.

    @ivar index: next index to use
    @type index: C{int}
    @ivar park_translate: dictionary of old to new parking id mappings
    @type park_translate: C{dict}
    @ivar turn_translate: dictionary of old to new turn id mappings
    @type turn_translate: C{dict}
    @ivar seg_translate: dictionary of old to new segment id mappings
    @type seg_translate: C{dict}
    @ivar stop_translate: dictionary of old to new stop id mappings
    @type stop_translate: C{dict}
    @ivar poi_translate: dictionary of old to new poi id mappings
    @type poi_translate: C{dict}
    @ivar ride_translate: dictionary of old to new ride id mappings
    @type ride_translate: C{dict}
    """

    def __init__(self, template_file=None, man=None):
        """
        Adds the "start" and "unique" options to the command-line options.

        @param template_file: (optional) file name of template file
        @type template_file: C{string}
        @param man: (optional) extended program help
        @type man: C{string}
        """
        SabxProcessor.__init__(self, template_file, man)

        self.parser.add_option("-s", "--start", dest="start",
                               help="number to start at", 
                               type="int", default=1, metavar="START")
        self.parser.add_option("-u", "--unique", dest="unique",
                               action="store_true",
                               help="all unique ids?", 
                               default=False, metavar="UNIQUE")

    def _create_item_translation(self, item_list):
        """
        Create the translation dictionary for an item list.
        """
        keys = [item.id for item in item_list]
        vals = self.id.range(len(item_list))
        trans = {}
        for key, val in zip(keys, vals):
            trans[key] = val
        return trans

    def _create_translations(self):
        """
        Read all the ids for parking places, turns, segments, stops, and pois
        and generate new ids for them, saving the mappings.
        """
        self.park_translate = self._create_item_translation(
            self.template_data['park_list'])
        self.turn_translate = self._create_item_translation(
            self.template_data['turn_list'])
        self.seg_translate = self._create_item_translation(
            self.template_data['seg_list'])
        self.stop_translate = self._create_item_translation(
            self.template_data['stop_list'])
        self.poi_translate = self._create_item_translation(
            self.template_data['poi_list'])
        self.ride_translate = self._create_item_translation(
            self.template_data['ride_list'])

    def _renumber_items(self, item_list, translater):
        """
        Renumber all the items in the list.
        """
        for item in item_list:
            item.id = translater[item.id]

    def _renumber_seg_pts_stops_pois(self, seg):
        """
        Renumber the stops and pois for a segment.
        """
        for pt in seg.waypoints:
            pt.id = self.id.next()

            if pt.stop:
                pt.stop = (' ').join([self.stop_translate[stop_item]
                                      for stop_item in pt.stop.split()])

            if pt.poi:
                pt.poi = (' ').join([self.poi_translate[poi_item]
                                     for poi_item in pt.poi.split()])

    def _renumber_ride_park_turns_segs(self, ride):
        """
        Renumber the parking, turns, and segments for a ride.
        """
        ride.parking = self.park_translate[ride.parking]
        ride.turns = [self.turn_translate[turn] for turn in ride.turns]
        ride.segs = [self.seg_translate[seg] for seg in ride.segs]

    def _renumber_ids(self):
        """
        Go through all the parking places, turns, segments, stops, pois, and
        rides and renumber them all.
        """
        self._renumber_items(self.template_data['park_list'], 
                             self.park_translate)
        self._renumber_items(self.template_data['turn_list'], 
                             self.turn_translate)
        self._renumber_items(self.template_data['seg_list'], 
                             self.seg_translate)
        self._renumber_items(self.template_data['stop_list'], 
                             self.stop_translate)
        self._renumber_items(self.template_data['poi_list'], 
                             self.poi_translate)
        self._renumber_items(self.template_data['ride_list'], 
                             self.ride_translate)

        self.id.reset()
        for seg in self.template_data['seg_list']:
            self._renumber_seg_pts_stops_pois(seg)

        for ride in self.template_data['ride_list']:
            self._renumber_ride_park_turns_segs(ride)

    def get_template_data(self):
        """
        Renumber all the ids for all the SABX 1.0 data.
        """
        SabxProcessor.get_template_data(self)
        self.id = Id(self.options.start, self.options.unique)
        self._create_translations()
        self._renumber_ids()
