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
Generate and place the map legend.  Look for a space in the map that doesn't
have any route items on it.  Cheat by splitting the map into 9 squares (3x3)
and check each square for ride items intersecting it.  Choose the square with
the least intersections, or an arbitrary one if there is a tie.
"""

from sabx10.oxm import Box, pt_dist_from_pt

from consts import PIX_SCALE_FACTOR

def _calc_box_lats(ride, legend_height):
    """
    Split the map into three equal pieces going top to bottom.

    @param ride: ride representing map to split
    @type ride: L{Ride}
    @param legend_height: height of legend
    @type legend_height: C{float}

    @return: bottom min, bottom max, middle min, middle max, top min, top max
    @rtype: C{float},C{float},C{float},C{float},C{float},C{float}
    """
    # bottom
    bottom_lat_min = ride.bounds.min_lat
    bottom_lat_max, lon = pt_dist_from_pt(ride.bounds.min_lat, 
                                          ride.bounds.min_lon, 
                                          legend_height, 0)

    # mid
    mid_lat = (ride.bounds.min_lat + ride.bounds.max_lat) / 2.0
    mid_dist = legend_height / 2.0
    mid_lat_min, lon = pt_dist_from_pt(mid_lat, ride.bounds.min_lon, 
                                  mid_dist, 180)
    mid_lat_max, lon = pt_dist_from_pt(mid_lat, ride.bounds.min_lon, 
                                  mid_dist, 0)

    # top
    top_lat_min, lon = pt_dist_from_pt(ride.bounds.max_lat, 
                                       ride.bounds.max_lon, 
                                       legend_height, 180)
    top_lat_max = ride.bounds.max_lat

    return bottom_lat_min, bottom_lat_max, \
        mid_lat_min, mid_lat_max, \
        top_lat_min, top_lat_max

def _calc_box_lons(ride, legend_width):
    """
    Split the map into three equal pieces going left to right.

    @param ride: ride representing map to split
    @type ride: L{Ride}
    @param legend_width: width of legend
    @type legend_width: C{float}

    @return: left min, left max, middle min, middle max, right min, right max
    @rtype: C{float},C{float},C{float},C{float},C{float},C{float}
    """
    # left
    left_lon_min = ride.bounds.min_lon
    lat, left_lon_max = pt_dist_from_pt(ride.bounds.min_lat, 
                                        ride.bounds.min_lon, 
                                        legend_width, 90)

    # mid
    mid_lon = (float(ride.bounds.min_lon) + float(ride.bounds.max_lon)) / 2.0
    mid_dist = legend_width / 2.0
    lat, mid_lon_min = pt_dist_from_pt(ride.bounds.min_lat, mid_lon, 
                                       mid_dist, 270)
    lat, mid_lon_max = pt_dist_from_pt(ride.bounds.min_lat, mid_lon, 
                                       mid_dist, 90)

    # right
    lat, right_lon_min = pt_dist_from_pt(ride.bounds.max_lat, 
                                         ride.bounds.max_lon, 
                                         legend_width, 270)
    right_lon_max = ride.bounds.max_lon

    return left_lon_min, left_lon_max, \
        mid_lon_min, mid_lon_max, \
        right_lon_min, right_lon_max

def _create_legend_boxes(ride, legend_width, legend_height):
    """
    Create the boxes to check against.  This is a 3x3 grid splitting the map
    into equal spaces.

    @param ride: ride representing map to split
    @type ride: L{Ride}
    @param legend_width: width of legend
    @type legend_width: C{float}
    @param legend_height: height of legend
    @type legend_height: C{float}

    @return: C{list} of boxes
    @rtype: C{list} of C{Box}
    """
    bottom_lat_min, bottom_lat_max, mid_lat_min, mid_lat_max, \
        top_lat_min, top_lat_max = _calc_box_lats(ride, legend_height)

    left_lon_min, left_lon_max, mid_lon_min, mid_lon_max, \
        right_lon_min, right_lon_max = _calc_box_lons(ride, legend_width)

    boxes = [Box(top_lat_min, left_lon_min, top_lat_max, left_lon_max), # top
             Box(top_lat_min, mid_lon_min, top_lat_max, mid_lon_max),
             Box(top_lat_min, right_lon_min, top_lat_max, right_lon_max),

             Box(mid_lat_min, left_lon_min, mid_lat_max, left_lon_max), # middle
             Box(mid_lat_min, mid_lon_min, mid_lat_max, mid_lon_max),
             Box(mid_lat_min, right_lon_min, mid_lat_max, right_lon_max),

             Box(bottom_lat_min, left_lon_min, bottom_lat_max, left_lon_max), # bottom
             Box(bottom_lat_min, mid_lon_min, bottom_lat_max, mid_lon_max),
             Box(bottom_lat_min, right_lon_min, bottom_lat_max, right_lon_max)]
    for the_box in boxes:
        the_box.count = 0

    return boxes

def _check_boxes_for_point(boxes, lat, lon):
    """
    Check the list of boxes to see which ones the point is in.  It really
    should only be in one box since we divided the map evenly.

    @param boxes: C{list} of boxes to check
    @type boxes: C{list} of L{Box}
    @param lat: latitude of point to check
    @type lat: C{float}
    @param lon: longitude of point to check
    @type lon: C{float}
    """
    for the_box in boxes:
        if the_box.is_pt_in_box(lat, lon):
            the_box.count += 1

def _check_boxes(boxes, ride):
    """
    Check the list of boxes against all the point items in the ride.  This
    includes segment waypoints, stops, pois, and parking.

    @param boxes: C{list} of boxes to check
    @type boxes: C{list} of L{Box}
    @param ride: ride representing map to check
    @type ride: L{Ride}
    """
    _check_boxes_for_point(boxes, 
                           ride.parking.lat, ride.parking.lon)

    for seg in ride.segs:
        for pt in seg.waypoints:
            _check_boxes_for_point(boxes, pt.lat, pt.lon)

    for stop in ride.stops:
        _check_boxes_for_point(boxes, stop.lat, stop.lon)

    for poi in ride.pois:
        _check_boxes_for_point(boxes, poi.lat, poi.lon)

def _find_legend_box(ride, legend_width, legend_height):
    """
    Check the map for a space to place the legend.

    @param ride: ride representing map to check
    @type ride: L{Ride}
    @param legend_width: width of legend
    @type legend_width: C{float}
    @param legend_height: height of legend
    @type legend_height: C{float}

    @return: C{list} of boxes in order of goodness
    @rtype: C{list} of L{Box}
    """
    boxes = _create_legend_boxes(ride, legend_width, legend_height)
    _check_boxes(boxes, ride)
    boxes.sort(key=lambda x: x.count)
    return boxes[0]

class LegendNode(object):
    """
    Holds one item in the legend, one item per legend line.

    @ivar id: id of item
    @type id: C{int}
    @ivar text: text of item
    @type text: C{string}
    @ivar lat: latitude of text top
    @type lat: C{float}
    @ivar lon: longitude of text left
    @type lon: C{float}
    """
    def __init__(self, id, text, lat, lon):
        """
        Save the passed-in values.

        @param id: id of item
        @type id: C{int}
        @param text: text of item
        @type text: C{string}
        @param lat: latitude of text top
        @type lat: C{float}
        @param lon: longitude of text left
        @type lon: C{float}
        """
        self.id = id
        self.text = text
        self.lat = lat
        self.lon = lon

def _gen_legend_item(lat, lon, text, dist, node_id):
    """
    Generate a L{LegendNode}, and calculate a point below it.  This allows us
    to generate the items and "walk" them down the page in the process.  We
    end-up with legend items on successive lines on the map page.

    @param lat: latitude of legend item
    @type lat: C{float}
    @param lon: longitude of legend item
    @type lon: C{float}
    @param text: text of legend item
    @type text: C{string}
    @param dist: distance down page for next item
    @type dist: C{float}
    @param node_id: L{NodeId} to generate id from
    @type node_id: L{NodeId}

    @return: L{LegendNode}, lat of next legend item, lon of next legend item
    @rtype: L{LegendNode},C{float},C{float}
    """
    node = LegendNode(node_id.next(), text, lat, lon)
    lat, lon = pt_dist_from_pt(lat, lon, dist, 180)

    return node, lat, lon

def generate_legend(the_ride, title, node_id):
    """
    Generate the legend items for the map for the given ride.

    @param the_ride: L{Ride} to generate the legend for
    @type the_ride: L{Ride}
    @param title: title for the map
    @type title: C{string}
    @param node_id: L{NodeId} to generate legend node ids from
    @type node_id: L{NodeId}
    """
    width_of_pix = the_ride.bounds.width() / the_ride.bounds.pix_width
    height_of_pix = the_ride.bounds.height() / the_ride.bounds.pix_height

    legend_width = 200.0 * width_of_pix * PIX_SCALE_FACTOR
    legend_height = 200.0 * height_of_pix * PIX_SCALE_FACTOR
    box = _find_legend_box(the_ride, legend_width, legend_height)

    lat = box.max_lat
    lon = (box.min_lon + box.max_lon) / 2.0
    #the_ride.logo_node, lat, lon = \
    #    _gen_legend_item(lat, lon, '', 
    #                 height_of_pix * 47 * PIX_SCALE_FACTOR, node_id)
    the_ride.title_node, lat, lon = \
        _gen_legend_item(lat, lon, title, 
                         height_of_pix * 20 * PIX_SCALE_FACTOR, node_id)
    the_ride.dist_node, lat, lon = \
        _gen_legend_item(lat, lon, "%.1f Mile Option" % the_ride.distance, 
                         height_of_pix * 18 * PIX_SCALE_FACTOR, node_id)
    the_ride.url_node, lat, lon = \
        _gen_legend_item(lat, lon, 'www.sabikerides.com', 
                         height_of_pix * 17 * PIX_SCALE_FACTOR, node_id)
    the_ride.park_node, lat, lon = \
        _gen_legend_item(lat, lon, 'parking in red', 
                         height_of_pix * 17 * PIX_SCALE_FACTOR, node_id)
    the_ride.turn_node, lat, lon = \
        _gen_legend_item(lat, lon, 'numbered turns in green', 
                         height_of_pix * 17 * PIX_SCALE_FACTOR, node_id)
    the_ride.stop_node, lat, lon = \
        _gen_legend_item(lat, lon, 'numbered stops in blue', 
                         height_of_pix * 17 * PIX_SCALE_FACTOR, node_id)
    the_ride.poi_node, lat, lon = \
        _gen_legend_item(lat, lon, 'numbered points of interest in yellow', 
                         height_of_pix * 17 * PIX_SCALE_FACTOR, node_id)
