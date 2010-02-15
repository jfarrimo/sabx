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
"""
Various constants and utility functions used by the SABX library.

@var cur_version: current version of the SABX file format (always "1.0" for 
the SABX10 library)
@type cur_version: C{string}
@var rad_to_nm: multiply a radian value by this to convert it to nautical miles
@type rad_to_nm: C{float}
@var nm_to_rad: multiply a nautical mile value by this to convert it to radians
@type nm_to_rad: C{float}
@var nm_to_statute: multiply a nautical mile value by this to convert it to 
statute miles
@type nm_to_statute: C{float}
@var statute_to_nm: multiply a statute mile value by this to convert it to 
nautical miles
@type statute_to_nm: C{float}
@var meter_feet: number of feet in a meter
@type meter_feet: C{float}
@var mile_feet: number of feet in a mile
@type mile_feet: C{float}
"""
from math import *
import xml.etree.ElementTree as et

############################################
# GREAT CIRCLE CALCULATIONS
############################################

rad_to_nm = 180 * 60 / pi
nm_to_rad = pi / (180 * 60)
nm_to_statute = 57875.0 / 50292.0
statute_to_nm = 50292.0 / 57875.0
meter_feet = 3.28083989501312
mile_feet = 5280.0
kilometer_miles = 0.621371192

def calculate_distance(lat1, lon1, lat2, lon2):
    ''' 
    Calculate the distance between the two points (C{lat1},C{lon1}) and
    (C{lat2},C{lon2}) in statute miles.

    @param lat1: decimal degrees
    @type lat1: C{float}
    @param lon1: decimal degrees (west is negative)
    @type lon1: C{float}
    @param lat2: decimal degrees
    @type lat2: C{float}
    @param lon2: decimal degrees (west is negative)
    @type lon2: C{float}

    @return: distance in statute miles
    @rtype: C{float}
    '''
    lat1 = radians(float(lat1))
    lon1 = radians(float(lon1))
    lat2 = radians(float(lat2))
    lon2 = radians(float(lon2))
    rad_dist = 2 * asin(
        sqrt(
            pow(sin((lat1-lat2)/2), 2) +
            cos(lat1) * cos(lat2) *
            pow(sin((lon1-lon2)/2),2)
            )
        )
    nm_dist = rad_dist * rad_to_nm
    return nm_dist * nm_to_statute

def pt_dist_from_pt(lat1, lon1, distance, true_course):
    """ 
    Calculate a point (C{lat},C{lon}) that is C{distance} statute miles
    from the point (C{lat1},C{lon1}) along a course C{true_course} degrees.

    Some useful C{true_course} values:
      - 0.0 - north
      - 90.0 - east
      - 180.0 - south
      - 270.0 - west

    @param lat1: decimal degrees
    @type lat1: C{float}
    @param lon1: decimal degrees (west is negative)
    @type lon1: C{float}
    @param distance: distance from the point in statute miles
    @type distance: C{float}
    @param true_course: true course from the point in degrees
    @type true_course: C{float}
    
    @return: (C{lat},C{lon}) representing the calculated point
    @rtype: (C{float},C{float})
    """
    # angle_radians=(pi/180)*angle_degrees
    distance = (distance * statute_to_nm) * nm_to_rad
    true_course = (pi / 180) * true_course
    lat1 = radians(lat1)
    lon1 = radians(-lon1)

    lat = asin( sin(lat1) * cos(distance) + cos(lat1) * 
                sin(distance) * cos(true_course) )
    if cos(lat) == 0.0:
        lon = lon1      # endpoint a pole
    else:
        lon = (
            (lon1 - asin( sin(true_course) * sin(distance) / cos(lat) ) + pi) % 
            (2*pi) ) - pi

    return degrees(lat), degrees(-lon)

############################################
# SABX VERSION
############################################

cur_version = "1.0"

class VersionException(Exception):
    """ 
    This exception is raised to indicate an incorrect SABX file version was
    encoutered.
    """
    pass

def check_version(xml_tree):
    """ 
    Check the version of the XML tree.

    @param xml_tree: an C{ElementTree} C{Element} that's the root of an SABX
    XML tree
    @type xml_tree: C{Element}

    @raise VersionException: when the given tree is not of the current version,
    this exception is raised

    @return: C{True} to indicate good version
    @rtype: C{boolean}
    """
    if xml_tree.attrib['version'] != cur_version:
        raise VersionException('Version %s of SABX format expected.' % 
                               cur_version)
    return True

############################################
# ELEMENTTREE UTILS
############################################

def get_from_id(elements, id):
    """
    Find an C{ElementTree} element with the given id in a list of elements.

    I can't believe element tree doesn't provide something like this.
    Actually, it looks like element tree 1.3 may provide something like this
    with their XPath support - I need to check this out.

    @param elements: C{list} of C{ElementTree} C{Element}s
    @type elements: C{list}
    @param id: id of element to find
    @type id: C{string}

    @return: C{Eement} found or C{None}
    @rtype: C{Element}
    """
    for element in elements:
        if element.attrib['id'] == id:
            return element
    return None

def parse_no_def_namespaces(source):
    """
    Read an XML file using C{ElementTree} tree, stripping default namespace
    strings from all elements.

    This routine is a little bit precarious.  Its aim is to strip the default
    namespace {uri} from tags so that you don't have to put all that text into
    find, findall, findtext, etc... when searching the XML tree using the
    C{ElementTree} stuff.

    This should work most of the time.  That is, when there is only one default
    namespace declared, in the root of the XML tree, then it will be just fine.
    In other instances, where the default namespace changes throughout the XML
    document, the behavior can be unexpected.

    Actually, the behavior of this function isn't unexpected.  It will work
    just fine.  It's the behaviour of anything using it that will be
    unexpected.  If you change default namespaces, and you have tags that have
    duplicate local portions that are differentiated by the namespace, then
    they will all be retrieved by the find... calls.  This may not be what you
    want.  Luckily, in the limited world that this routine operates in (so
    far), this isn't a problem.  GPX, TCX, and SABX files all have one default
    namespace, declared in the root element.  Let's hope.

    @param source: XML file to read
    @type source: C{string} or open file handle

    @return: tree root C{Element} (B{NOT} an C{ElementTree} object)
    @rtype: C{Element}
    """
    events = ("start", "end", "start-ns")
    root = None
    def_namespace = ""
    for event, elem in et.iterparse(source, events=events):
        if event == "start":
            if root is None:
                root = elem
        elif event == "start-ns":
            if elem[0] == '':
                if elem[1]:
                    def_namespace = "{%s}" % elem[1]
                else:
                    def_namespace = ""
        else:
            if def_namespace:
                elem.tag = elem.tag.replace(def_namespace, "")
    return root
