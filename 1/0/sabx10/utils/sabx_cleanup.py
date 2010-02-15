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
Handle cleaning-up SABX files.
"""

from sabx10.templating import SabxProcessor

class CleanupProcessor(SabxProcessor):
    """
    Process an SABX 1.0 file and remove all unused parking places, turns,
    segments, stops, and pois.

    @ivar used_parking_ids: list of parking place ids used in rides
    @type used_parking_ids: C{list} of C{string}
    @ivar used_turn_ids: list of turn ids used in rides
    @type used_turn_ids: C{list} of C{string}
    @ivar used_seg_ids: list of segment ids used in rides
    @type used_seg_ids: C{list} of C{string}
    @ivar used_stop_ids: list of stop ids used in rides
    @type used_stop_ids: C{list} of C{string}
    @ivar used_poi_ids: list of poi ids used in rides
    @type used_poi_ids: C{list} of C{string}
    """

    def _get_used_item_ids(self):
        """
        Go through all the rides in the rideset and make lists of all parking
        places, turns, segments, stops, and pois that are used.
        """
        self.used_parking_ids = []
        self.used_turn_ids = []
        self.used_seg_ids = []
        self.used_stop_ids = []
        self.used_poi_ids = []

        for ride in self.template_data['ride_list']:
            self.used_parking_ids.append(ride.parking)
            self.used_turn_ids.extend(ride.turns)
            self.used_seg_ids.extend(ride.segs)

        for seg_index in self.used_seg_ids:
            for pt in self.template_data['seg_dict'][seg_index].waypoints:
                if pt.stop is not None:
                    stop_list = pt.stop.split(',')
                    self.used_stop_ids.extend(stop_list)

                if pt.poi is not None:
                    poi_list = pt.poi.split(',')
                    self.used_poi_ids.extend(poi_list)

    def _get_used_items(self, old_list, used_ids):
        """
        Go through items in the old_list and make a new list and dict
        containing the items whose ids are in used_ids.

        @param old_list: list of items to check
        @type old_list: C{list} of objects
        @param used_ids: list of ids to check against
        @type used_ids: C{list} of C{string}

        @return: C{list} and C{dict} of used items
        @rtype: (C{list}, C{dict}) of used objects
        """
        used_list = []
        used_dict = {}
        for item in old_list:
            if item.id in used_ids:
                used_list.append(item)
                used_dict[item.id] = item
        return used_list, used_dict

    def _cull_unused_items(self):
        """
        Go through the lists of parking places, turns, segments, stops, and
        pois and only keeps items that are used in rides.
        """
        self.template_data['park_list'], self.template_data['park_dict'] = \
            self._get_used_items(
            self.template_data['park_list'], self.used_parking_ids)
        self.template_data['turn_list'], self.template_data['turn_dict'] = \
            self._get_used_items(
            self.template_data['turn_list'], self.used_turn_ids)
        self.template_data['seg_list'], self.template_data['seg_dict'] = \
            self._get_used_items(
            self.template_data['seg_list'], self.used_seg_ids)
        self.template_data['stop_list'], self.template_data['stop_dict'] = \
            self._get_used_items(
            self.template_data['stop_list'], self.used_stop_ids)
        self.template_data['poi_list'], self.template_data['poi_dict'] = \
            self._get_used_items(
            self.template_data['poi_list'], self.used_poi_ids)

    def get_template_data(self):
        """
        Culls unused items from the SABX 1.0 data.
        """
        SabxProcessor.get_template_data(self)
        self._get_used_item_ids()
        self._cull_unused_items()
