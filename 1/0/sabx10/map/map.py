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
Main code for generating interactive Google Maps representations of SABX data
files.  It takes an SABX file and parses it and processes its rides using the
L{sabx10.oxm} package.  It then adds additional data to the processed rides.

@var zoom_levels: distances between 32x32 map icons in Google Maps for each zoom 
level, with the zoom level being the index of the distance in the list
@type zoom_levels: C{list}
"""
import os.path
import sys

import sabx10.oxm as oxm
from sabx10.templating import TemplateProcessor

from consts import BORDER
from elevations import process_elevations
import glineenc

#### ZOOM LEVEL ####
zoom_levels = [2690, 1354, 680, 342, 168, 86, 42, 21, 11, 
               5.3, 2.6, 1.32, 0.66, 0.33, 0.17, 0.083, 
               0.041, 0.021, 0.01, 0.005]

def _min_distance(points, pt):
    """
    Determine how far away, in statute miles, the closest point to C{pt} is in
    C{points}.

    @param points: C{list} of points to check against
    @type points: C{list} of L{Point} objects
    @param pt: L{Point} object to check for
    @type pt: L{Point} object

    @return: distance to closest point
    @rtype: C{float}
    """
    min_dist = 3000
    for point in points:
        min_dist = min(min_dist, pt.calculate_distance(point))
    return min_dist

def _min_zoom_level(points, pt):
    """
    Determine the minimum Google maps zoom level to show C{pt} so that it won't
    overlap with other points in the C{points} list at higher zooms.  This
    assumes lower zoom levels show bigger areas, such that the highest zoom
    level would show a tick on a rat's back, while the lowest zoom level would
    show the continents of the world.  Lowest is 0, while highest is 19. These
    are determined so that 32x32 icons won't overlap in the area of the map
    surrounding San Antonio, TX.  For other parts of the world (closer or
    farther from the equator) these values may not be all that good.

    @param points: C{list} of points to check against
    @type points: C{list} of L{Point} objects
    @param pt: L{Point} object to check for
    @type pt: L{Point} object

    @return: zoom level
    @rtype: C{int}
    """
    dist = _min_distance(points, pt)
    index = 0
    for zoom in zoom_levels:
        if dist > zoom:
            return index
        index += 1
    return index

#### SEGMENTS & TURNS ####
def _process_segments(ride_segs, graph_filebase, ride_index):
    """
    For each segment in a ride, give it a type, Google Map encode its points,
    and add filenames for its profiles.

    Set the type to "seg", so that Jinja2 can tell what type it is, since
    Jinja2 doesn't natively support object introspection.

    Add encoded points, meaning points that have been encoded into Google Maps'
    compact format for storing segment points.

    Add filenames for the profiles for the segments.

    @param ride_segs: list of segments in the ride
    @type ride_segs: C{list} of L{Segment} objects
    @param graph_filebase: base name for profile files
    @type graph_filebase: C{string}
    @param ride_index: index of ride being processed
    @type ride_index: C{string}
    """
    for seg in ride_segs:
        # encode points
        pts = [(pt.lat, pt.lon) for pt in seg.waypoints]
        seg.encoded_points, seg.encoded_levels = glineenc.encode_pairs(pts)

        # type of 'seg'
        seg.item_type = 'seg'

        # create filenames
        seg.profile_small = '%s_prof_small_%s_%s.png' % \
            (graph_filebase, ride_index, seg.index)
        seg.profile_large = '%s_prof_large_%s_%s.png' % \
            (graph_filebase, ride_index, seg.index)

def _process_turns(ride_turns):
    """
    For each turn in a ride, set its type and calculate a zoom level.

    Calculate the minimum Google Maps zoom level to display this turn.

    Set the type to "turn" so that Jinja2 can tell what type it is, since
    Jinja2 doesn't natively support object introspection.

    @param ride_turns: list of turns for this ride
    @type ride_turns: C{list} of L{Turn} objects
    """
    turn_points = []
    for turn in ride_turns:
        # handle zoom level
        turn_point = oxm.Point(turn.lat, turn.lon)
        turn.min_zoom = _min_zoom_level(turn_points, turn_point)
        turn_points.append(turn_point)

        # type of 'turn'
        turn.item_type = 'turn'

#### STOPs & POIs ####
def _process_stops(ride_stops):
    """
    For each stop in a ride, set its type.

    Set the type to "stop" so that Jinja2 can tell what type it is, since
    Jinja2 doesn't natively support object introspection.

    @param ride_stops: list of stops to process
    @type ride_stops: C{list} of L{Stop} objects
    """
    for stop in ride_stops:
        stop.item_type = 'stop'

def _process_pois(ride_pois):
    """
    For each poi in a ride, set its type.

    Set all the pois to have type "poi" so that Jinja2 can tell what type it
    is, since Jinja2 doesn't natively support object introspection.

    @param ride_pois: list of pois to process
    @type ride_pois: C{list} of L{Poi} objects
    """
    for poi in ride_pois:
        poi.item_type = 'poi'

def _process_stop_poi_dists(item_list):
    """
    Calculate the ride distance and off-course distance for each poi or stop in
    a ride.  This function works on stop or poi lists, and expects one of these
    to be passed in.

    Go through the list of stops/pois for a ride and correlate these with the
    stops/pois defined for the rideset.  For each occurrence of a stop/poi in a
    ride, save the distance into the ride and the distance off course for the
    stop/poi. You want to do this because a single stop/poi can be used several
    times in a ride.  When summarizing the stop/poi, you want to be able to
    list all the distances for the stop/poi.  This is used when generating the
    stop/poi info dialog when clicking on the stop/poi icon in the Google Map.

    @param item_list: list of items to process
    @type item_list: C{list} of L{Poi} or L{Stop} objects

    @return: distances dictionary
    @rtype: C{dictionary}
    """
    item_dists = {}
    for item in item_list:
        if item.id in item_dists:
            item_dists[item.id].append((item.distance,item.off_route))
        else:
            item_dists[item.id] = [(item.distance,item.off_route)]
    return item_dists

#### MAIN ####
def _process_all_rides(xml_tree, filebase):
    """
    Go through all the rides in the rideset and update them with the extra
    information necessary to correctly render maps and their data from the
    templates.

    @param xml_tree: C{ElementTree} representation of a rideset
    @type xml_tree: C{ElementTree} stuff
    @param filebase: base upon which to build file names
    @type filebase: C{string}

    @return: modified ride data
    @rtype: C{list} of L{Ride}
    """
    ride_data, bounds = oxm.process_rides(xml_tree)
    for ride in ride_data:
        # basic processing
        _process_segments(ride.segs, filebase, ride.index)
        _process_turns(ride.turns)
        _process_stops(ride.stops)
        _process_pois(ride.pois)

        # stop/poi distances
        ride.stop_dists = _process_stop_poi_dists(ride.stops)
        ride.poi_dists = _process_stop_poi_dists(ride.pois)

        # elevations
        ride.ele, ride.ele_segs = process_elevations(ride)

        # file names
        ride.profile_small = \
            '%s_prof_small_%s_all.png' % (filebase, ride.index)
        ride.profile_large = \
            '%s_prof_large_%s_all.png' % (filebase, ride.index)
        ride.map_large = '%s_map_%s.png' % (filebase, ride.index)
        ride.map_small_base = '%s_map_%s_' % (filebase, ride.index)

    return ride_data

class SabxProcessor(TemplateProcessor):
    """
    Specialized L{TemplateProcessor} to handle SABX files and turn them into
    Google Maps displayable maps.
    """

    def __init__(self, template_file=None, man=None):
        """
        Add command-line options to set the input file and various directories
        the templates need to know about.

        @param template_file: name of template file to process
        @type template_file: C{string}
        @param man: man page text
        @type man: C{string}
        """
        TemplateProcessor.__init__(self, template_file, man)

        # input file
        self.parser.add_option("-i", "--infile", dest="in_file",
                               help="input sabx data from FILE", 
                               metavar="FILE")

        # directories
        self.parser.add_option("-r", "--marker-dir", dest="marker_dir",
                               help="relative web directory for marker files", 
                               metavar="MARKERDIR", default=".")
        self.parser.add_option("-g", "--image-dir", dest="image_dir",
                               help="relative web directory for image files", 
                               metavar="IMAGEDIR", default=".")
        self.parser.add_option("-c", "--css-dir", dest="css_dir",
                               help="relative web directory for css files", 
                               metavar="CSSDIR", default=".")
        self.parser.add_option("-j", "--js-dir", dest="js_dir",
                               help="relative web directory for javascript files", 
                               metavar="JSDIR", default=".")
        self.parser.add_option("-b", "--base-dir", dest="base_dir",
                               help="relative base web directory", 
                               metavar="BASEDIR", default=".")
        self.parser.add_option("-a", "--analytics-key", dest="analytics",
                               help="Google analytics key", 
                               metavar="ANALYTICS", default="")

    def process_options(self):
        """
        Save the dirs and setup for the input and output files.
        """
        def _save_options(self):
            self.template_data['marker_dir'] = self.options.marker_dir
            self.template_data['image_dir'] = self.options.image_dir
            self.template_data['css_dir'] = self.options.css_dir
            self.template_data['js_dir'] = self.options.js_dir
            self.template_data['base_dir'] = self.options.base_dir
            self.template_data['analytics'] = self.options.analytics

        def _setup_input_file(self):
            if self.options.in_file:
                self.in_file = open(self.options.in_file, "r")
            else:
                self.in_file = sys.stdin

        def _setup_output_file(self):
            if self.options.out_file:
                self.filebase = \
                    os.path.splitext(os.path.basename(self.options.out_file))[0]
                self.filebase = self.filebase.replace("-print", "")
            else:
                self.filebase = "stdout"

        TemplateProcessor.process_options(self)
        _save_options(self)
        _setup_input_file(self)
        _setup_output_file(self)

    def get_template_data(self):
        """
        Add all the extra-special goodness to the SABX data for our templates.
        """
        xml_tree = oxm.parse_no_def_namespaces(self.in_file)
        self.template_data.update(oxm.parse_top_level(xml_tree))
        self.template_data['filebase'] = self.filebase
        self.template_data['photos'] = oxm.parse_photos(xml_tree)
        self.template_data['rides'] = \
            _process_all_rides(xml_tree, self.filebase)
        self.template_data['zoom_factor'] = glineenc.zoom_factor
        self.template_data['zoom_levels'] = glineenc.num_levels
        self.template_data['BORDER'] = BORDER
