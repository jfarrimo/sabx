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
Co-ordinate the generation of profiles for a rideset.
"""
from sabx10.oxm import parse_no_def_namespaces, meter_feet, process_rides

from consts import PROFILE_PPI, PROFILE_PDF_PPI
from plotter import ProfilePlotter

def _calc_elevation(ele):
    """
    Convert an elevation from meters to feet.

    @param ele: elevation to convert
    @type ele: C{float}

    @return: elevation in feet
    @rtype: C{float}
    """
    return (ele * meter_feet)

def _process_points(points, length):
    """
    For a list of points representing a line, generate lists of the elevations 
    and distances along the line for each point.

    @param points: points to process
    @type points: C{list} of L{Point}
    @param length: length of line the points represent
    @type length: C{float}

    @return: distances list, elevations list
    @rtype: (C{list} of C{float},C{list} of C{float})
    """
    dist = 0.0
    distances = []
    elevations = []

    for index in range(len(points)-1):
        elevation = _calc_elevation(points[index].ele)
        distance = points[index].calculate_distance(points[index+1])
            
        elevations.append(elevation)
        distances.append(dist)

        dist += distance

    distances.append(length)
    elevations.append(_calc_elevation(points[-1].ele))

    return distances, elevations

def _process_segs(plotter, segs):
    """
    Plot a large and a small profile for each segment in a list. These profiles
    are not annotated.

    @param plotter: L{ProfilePlotter} to generate the plots
    @type plotter: L{ProfilePlotter}
    @param segs: C{list} of L{Segment}s to process
    @type segs: C{list} of L{Segment} objects
    """
    for seg in segs:
        distances, elevations = _process_points(seg.waypoints, seg.length)
        plotter.plot_large_profile(distances, elevations, seg.length, seg.index)
        plotter.plot_small_profile(distances, elevations, seg.length, seg.index)

class Annotation(object):
    """
    Hold all information necessary for a profile annotation.

    @ivar text: text of annotation
    @type text: C{string}
    @ivar dist: distance into ride of annotation (X value)
    @type dist: C{float}
    @ivar ele: elevation of annotation (Y value)
    @type ele: C{float}
    """
    def __init__(self, text, dist, ele):
        """
        Save the passed-in values.

        @param text: text of annotation
        @type text: C{string}
        @param dist: distance into ride of annotation (X value)
        @type dist: C{float}
        @param ele: elevation of annotation (Y value)
        @type ele: C{float}
        """
        self.text = text
        self.dist = dist
        self.ele = ele

def _process_annotations(segs):
    """
    Generate the annotations for a list of segments.

    @param segs: C{list} of L{Segment}s to process
    @type segs: C{list} of L{Segment} objects

    @return: list of L{Annotation} objects
    @rtype: C{list} of L{Annotation} objects
    """
    return [Annotation("%s-%s" % (seg.index, 
                                  seg.road.split('/')[0][:20]),
                       seg.start_dist, 
                       _calc_elevation(seg.waypoints[0].ele))
            for seg in segs]

def _process_ride(plotter, ride):
    """
    Generate the large and small profiles for a ride.  Large ride profiles
    include annotations.

    @param plotter: L{ProfilePlotter} to generate the plots
    @type plotter: L{ProfilePlotter}
    @param ride: L{Ride} to process
    @type ride: L{Ride}
    """
    points = []
    for seg in ride.segs:
        points.extend(seg.waypoints)

    distances, elevations = _process_points(points, ride.distance)
    annotations = _process_annotations(ride.segs)

    plotter.plot_large_profile(distances, elevations, ride.distance, 
                               annotations=annotations)
    plotter.plot_small_profile(distances, elevations, ride.distance)

def plot_all_rides(xml_tree, graph_filebase, graph_dir, hires, segs):
    """
    Generate profiles for all the rides in a rideset, and all the rides'
    segments as well (if asked).

    @param xml_tree: C{ElementTree} representation of a rideset
    @type xml_tree: C{ElementTree} stuff
    @param graph_filebase: base filename for profile plots
    @type graph_filebase: C{string}
    @param graph_dir: directory to place profile plots into
    @type graph_dir: C{string}
    @param hires: high resolution?
    @type hires: C{boolean}
    @param segs: plot segments?
    @type segs: C{boolean}
    """
    if hires:
        ppi = PROFILE_PDF_PPI
    else:
        ppi = PROFILE_PPI

    ride_list, bounds = process_rides(xml_tree)
    for ride in ride_list:
        plotter = ProfilePlotter(ride, graph_filebase, graph_dir, ppi)
        if segs:
            _process_segs(plotter, ride.segs)
        _process_ride(plotter, ride)
