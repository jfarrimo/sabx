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
Create the template data and process the templates so that OSM format XML files
can be generated.  These files will later be processed by Mapnik into PDF files
containing ride maps.
"""
import math
import sys

from sabx10.map import BORDER
from sabx10.oxm import parse_segments, parse_top_level, process_rides, \
    parse_no_def_namespaces
from sabx10.templating import TemplateProcessor

from bounds import Bounds, Cluster
from consts import HEIGHT, WIDTH, PPI, PIX_SCALE_FACTOR
from legend import generate_legend
from utils import BaseId, NodeId
from zoom import find_close_item, get_zoom_items

#### SEGMENTS ####
def _process_segments(ride):
    """
    Go through all the segments for the ride and add way ids. This is necessary
    because the OSM way elements are generated from SABX segments and must have
    unique ids.

    @param ride: L{Ride} whose segments will be modified
    @type ride: L{Ride}
    """
    way_id = BaseId()
    for seg in ride.segs:
        seg.way_id = way_id.next()

#### TURNS ####
def _process_turns(ride, node_id):
    """
    Go through all the turns for the ride and add node ids. This is necessary
    because some OSM node elements are generated from SABX turns and must have
    unique ids. Also, add a name to the turn because all nodes are expected to
    have names.

    @param ride: L{Ride} whose turns will be modified
    @type ride: L{Ride}
    @param node_id: L{NodeId} to generate turn node ids from
    @type node_id: L{NodeId}
    """
    for turn in ride.turns:
        if turn.index == 0:
            turn.name = 'P'
        else:
            turn.name = turn.index
        turn.node_id = node_id.next()

#### TURN CLUSTERS ####
def _find_clustered_turns(turns, dist):
    """
    Find clusters of turns that are within "dist" distance of eachother.
    Clusters are used to create smaller maps of turns whose icons would overlap
    on the large map and be hard to distinguish.  These are like insets on some
    maps used to show highly detailed areas of interest.

    @param turns: C{list} of L{Turn}s to process
    @type turns: C{list} of L{Turn}
    @param dist: distance threshold for determining clusters
    @type dist: C{float}

    @return: C{list} of L{Cluster}
    @rtype: C{list} of L{Cluster}
    """
    dist /= 2.0
    clusters = []
    for turn in turns:
        old_cluster = find_close_item(clusters, turn, dist)
        if old_cluster is not None:
            old_cluster.expand_to_point(turn.lat, turn.lon)
        else:
            new_cluster = Cluster(turn.lat, turn.lon)
            clusters.append(new_cluster)

    clusters = [cluster for cluster in clusters if cluster.point_count > 1]
    for index, cluster in enumerate(clusters):
        cluster.index = index

    return clusters

def _size_cluster_bounding_boxes(clusters, dist):
    """
    Enlarge and set the pixel size for the L{Cluster} boxes.

    @param clusters: C{list} of L{Cluster}s to process
    @type clusters: C{list} of L{Cluster}
    @param dist: distance threshold for determining clusters
    @type dist: C{float}
    """
    for cluster in clusters:
        dist *= 1.1
        cluster.resize(dist, dist)
        cluster.set_pixel_size()

def _get_turn_clusters(turns, dist):
    """
    Generate and size the clusters for a list of turns.

    @param turns: C{list} of L{Turn}s to process
    @type turns: C{list} of L{Turn}
    @param dist: distance threshold for determining clusters
    @type dist: C{float}

    @return: C{list} of L{Cluster}
    @rtype: C{list} of L{Cluster}
    """
    clusters = _find_clustered_turns(turns, dist)
    _size_cluster_bounding_boxes(clusters, dist)
    return clusters

#### STOPS AND POIS ####
def _process_stops_pois(items, node_id):
    """
    Go through a list of stops or pois, filter out duplicates, and add node ids
    to them.
    
    Adding node ids is necessary because some OSM node elements are generated
    from SABX stops and pois and must have unique ids.

    Filtering out duplicates is necessary because some stops and pois can be
    visited more than once in a ride if a ride passes through the same place
    twice (or more).  For the map, the stop or poi icon should only be
    displayed once.

    @param items: C{list} of L{Stop} or L{Poi} items
    @type items: C{list} of L{Stop} or L{Poi}
    @param node_id: L{NodeId} to generate stop and poi node ids from
    @type node_id: L{NodeId}
    """
    item_ids = []
    filtered_items = []
    for item in items:
        if item.id not in item_ids:
            item_ids.append(item.id)
            item.node_id = node_id.next()
            filtered_items.append(item)
    return filtered_items

#### PARKING ####
def _process_parking(ride, node_id):
    """
    Update the parking for a ride by adding a node id. This is necessary
    because some OSM node elements are generated from SABX parking elements and
    must have unique ids.

    @param ride: L{Ride} whose parking will be modified
    @type ride: L{Ride}
    @param node_id: L{NodeId} to generate the parking node id from
    @type node_id: L{NodeId}
    """
    ride.parking.node_id = node_id.next()

#### ALL ####
def _process_zooms_n_clusters(the_ride, node_id):
    """
    Go through the given ride and generate turn clusters and lists of zoomed-in
    and zommed-out turns, stops, and pois.

    @param the_ride: L{Ride} to be processed
    @type the_ride: L{Ride}
    @param node_id: L{NodeId} to generate the node ids from
    @type node_id: L{NodeId}
    """
    icon_width = 10 * PIX_SCALE_FACTOR
    icon_height = 10 * PIX_SCALE_FACTOR

    sep_dist = the_ride.bounds.calc_sep_dist(icon_width, icon_height)
    the_ride.zoom_out_turns = get_zoom_items(the_ride.turns, sep_dist, node_id)
    the_ride.zoom_out_stops = get_zoom_items(the_ride.stops, sep_dist, node_id)
    the_ride.zoom_out_pois = get_zoom_items(the_ride.pois, sep_dist, node_id)

    the_ride.turn_clusters = _get_turn_clusters(the_ride.turns, sep_dist * 2.0)
    if len(the_ride.turn_clusters) > 0:
        sep_dist = the_ride.turn_clusters[0].calc_sep_dist(icon_width, 
                                                           icon_height)
        the_ride.zoom_in_turns = get_zoom_items(
            the_ride.turns, sep_dist, node_id)
        the_ride.zoom_in_stops = get_zoom_items(
            the_ride.stops, sep_dist, node_id)
        the_ride.zoom_in_pois = get_zoom_items(
            the_ride.pois, sep_dist, node_id)
    else:
        the_ride.zoom_in_turns = []
        the_ride.zoom_in_stops = []
        the_ride.zoom_in_pois = []

def _process_all_rides(xml_tree, title, node_id):
    """
    Go through all the rides in the rideset and generate the data needed by the
    template to create the PDF map data.

    @param xml_tree: C{ElementTree} representation of a rideset
    @type xml_tree: C{ElementTree} stuff
    @param title: title for the map
    @type title: C{string}
    @param node_id: L{NodeId} to generate the node ids from
    @type node_id: L{NodeId}
    """
    ride_data, bounds = process_rides(xml_tree)
    for ride in ride_data:
        _process_parking(ride, node_id)
        _process_segments(ride)
        _process_turns(ride, node_id)
        ride.stops = _process_stops_pois(ride.stops, node_id)
        ride.pois = _process_stops_pois(ride.pois, node_id)

        ride.bounds = Bounds(box=ride.bounds)
        ride.bounds.set_pixel_size()
        ride.bounds.expand_to_good_size(0.1)
        bounds.expand_to_box(ride.bounds)

        _process_zooms_n_clusters(ride, node_id)
        generate_legend(ride, title, node_id)

    return ride_data, bounds

class SabxProcessor(TemplateProcessor):
    """
    Specialized L{TemplateProcessor} to handle SABX files and turn them into
    map data that Mapnik can handle.
    """
    def __init__(self, template_file=None, man=None):
        """
        Add command-line option for input file.

        @param template_file: name of template file to process
        @type template_file: C{string}
        @param man: man page text
        @type man: C{string}
        """
        TemplateProcessor.__init__(self, template_file, man)

        self.parser.add_option("-i", "--infile", dest="in_file",
                               help="input sabx data from FILE", 
                               metavar="FILE")

    def process_options(self):
        """
        Setup for the input file.
        """
        TemplateProcessor.process_options(self)
        if self.options.in_file:
            self.in_file = open(self.options.in_file, "r")
        else:
            self.in_file = sys.stdin

    def get_template_data(self):
        """
        Add all the extra data that Mapnik needs.
        """
        xml_tree = parse_no_def_namespaces(self.in_file)
        self.template_data.update(parse_top_level(xml_tree))

        self.template_data['seg_list'], \
            self.template_data['seg_dict'] = parse_segments(xml_tree)
        node_id = NodeId(self.template_data['seg_list'])
        self.template_data['rides'], self.template_data['bounds'] = \
            _process_all_rides(xml_tree, self.template_data['title'], node_id)
        self.template_data['PIX_SCALE_FACTOR'] = PIX_SCALE_FACTOR
        self.template_data['PPI'] = PPI
        self.template_data['WIDTH'] = WIDTH
        self.template_data['HEIGHT'] = HEIGHT
        self.template_data['BORDER'] = BORDER
