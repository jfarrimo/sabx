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
Handle zoom levels for stops, pois, and turns.  It turns out that all three are
sufficiently similar that they can be processed generically.
"""

def find_close_item(item_list, check_item, dist):
    """
    Find the first item in item_list closer to the check_item than dist.

    @param item_list: C{list} of L{Point} items to check
    @type item_list: C{list} of L{Point}
    @param check_item: L{Point} to check against
    @type check_item: L{Point}
    @param dist: threshhold distance to check for
    @type dist: C{float}
    """
    for item in item_list:
        if check_item.calculate_distance(item) <= dist:
            return item

    return None

class ZoomItem(object):
    """
    Item referencing several non-zoomed items.
    
    @ivar lat: latitude
    @type lat: C{float}
    @ivar lon: longitude
    @type lon: C{float}
    @ivar node_id: id of this item
    @type node_id: C{int}
    @ivar name: name of this item
    @type name: C{string}
    """
    def __init__(self, lat, lon, node_id, name):
        """
        Save the passed-in values

        @param lat: latitude
        @type lat: C{float}
        @param lon: longitude
        @type lon: C{float}
        @param node_id: id
        @type node_id: C{int}
        @param name: name
        @type name: C{string}
        """
        self.lat = lat
        self.lon = lon
        self.node_id = node_id
        self.name = name

def get_zoom_items(items, dist, node_id):
    """
    Generate a "compacted" list of items based on a full item list.  This finds
    all items that are close to eachother, within a distance of "dist", and
    creates one item that references all of the close items.  This is good when
    a map would show a bunch of hard-to-read overlapping items at a spot, but
    will now show one single item instead.

    @param items: list of items to compact
    @type items: C{list} of L{Point} items
    @param dist: threshold distance between items
    @type dist: C{float}
    @param node_id: L{NodeId} object to get ids for zoomed items
    @type node_id: L{NodeId}
    """
    zoomed_items = []

    # process segs
    for index, item in enumerate(items):
        old_item = find_close_item(zoomed_items, item, dist)
        if old_item is not None:
            old_item.name = "%s,%s" % (old_item.name, index+1)
        else:
            new_item = ZoomItem(item.lat, item.lon, node_id.next(), index+1)
            zoomed_items.append(new_item)

    return zoomed_items
