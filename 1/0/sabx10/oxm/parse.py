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
Take an SABX XML tree and turn it into objects.

L{parse_tree} is the main entry point for parsing XML.  When you pass it an XML
tree of SABX data, it returns a dictionary of information corresponding to the
structure of an SABX file.  It's returned as a C{dict} because I generally use
this to read an SABX file, modify it, then run it through a Jinja2 template for
output.  Jinja2 takes a dictionary to pass to the template as it's template
data.

Here's a somewhat graphical representation of the data that you get back from
L{parse_tree}.

 - SABX - C{dict}
  - uuid
  - version
  - zip_prefix
  - desc
  - ride_type
  - title
  - description
  - terrain
  - photos - L{PhotoSet}
    - C{list} of L{Photo}
  - park_list and park_dict - C{list} and C{dict}
    - contains L{Parking}
  - turn_list and turn_dict - C{list} and C{dict}
    - contains L{Turn}
  - seg_list and seg_dict - C{list} and C{dict}
    - contains L{Segment}
      - C{list} of L{Waypoint}
        - stop ids
        - poi ids
  - stop_list and stop_dict - C{list} and C{dict}
    - contains L{Stop}
  - poi_list and poi_dict - C{list} and C{dict}
    - contains L{Poi}
  - ride_list and ride_dict - C{list} and C{dict}
    - contains L{Ride}
      - id
      - description
      - parking id
      - turns - C{list}
        - contains turn ids
      - segments - C{list}
        - contains segment ids
  - history - C{list}
    - contains L{HistoryUpdate}
"""

import xml.etree.ElementTree as et
from utils import check_version
from parking import parse_parking
from turn import parse_turns
from segment import parse_segments
from stop import parse_stops
from poi import parse_pois
from ride import parse_rides

############################################################
# PHOTOS
############################################################

class Photo(object):
    """ 
    A C{Photo} object holds the information for an "a" HTML element that
    links to photos of the ride.

    @ivar desc: description of what this links to
    @type desc: C{string}
    @ivar href: URL of the link
    @type href: C{string}
    """
    def __init__(self, desc, href):
        """
        Save the passed-in data.

        @param desc: description of what this links to
        @type desc: C{string}
        @param href: URL of the link
        @type href: C{string}
        """
        self.desc = desc
        self.href = href

class PhotoSet(object):
    """ 
    A C{PhotoSet} object holds information about a cover photo for the
    rideset and links to additional photos of the ride.

    @ivar title: title (hover) text for cover photo
    @type title: C{string}
    @ivar src: URL of cover photo
    @type src: C{string}
    @ivar photo_list: C{list} of C{Photo} objects
    @type photo_list: C{list} of C{Photo}
    """
    def __init__(self, title, src, photo_list):
        """
        Save the passed-in data.

        @param title: title (hover) text for cover photo
        @type title: C{string}
        @param src: URL of cover photo
        @type src: C{string}
        @param photo_list: C{list} of C{Photo} objects
        @type photo_list: C{list} of C{Photo}
        """
        self.title = title
        self.src = src
        self.photo_list = photo_list

def _parse_photos_photo(xml_photos):
    """
    Take the C{Element} for a photos element and turn it into a list of
    L{Photo} objects.

    @param xml_photos: C{Element} for the C{PhotoSet} element
    @type xml_photos: C{Element}

    @return: C{list} of L{Photo} objects
    @rtype: C{list} of L{Photo}
    """
    return [Photo(xml_photo.findtext('desc'), xml_photo.findtext('href'))
            for xml_photo in xml_photos.findall('photo')]

def parse_photos(xml_tree):
    """
    Parse the photos element in the given C{Element} tree.

    @param xml_tree: root of C{Element} tree that has photos
    @type xml_tree: C{Element} or C{ElementTree}

    @return: a C{PhotoSet} object or None
    @rtype: C{PhotoSet}
    """
    check_version(xml_tree)
    xml_photos = xml_tree.find('photos')
    if xml_photos:
        return PhotoSet(xml_photos.findtext('title'), 
                        xml_photos.findtext('src'),
                        _parse_photos_photo(xml_photos))
    else:
        return None

############################################################
# HISTORY
############################################################

class HistoryUpdate(object):
    """ 
    A C{HistoryUpdate} object holds the information for a single update to
    the SABX file.

    @ivar version: version number of the change
    @type version: C{string}
    @ivar date: date the change was made
    @type date: C{string}
    @ivar description: description of what the change entailed
    @type description: C{string}
    """
    def __init__(self, version, date, description):
        """
        Save the passed-in data.

        @param version: version number of the change
        @type version: C{string}
        @param date: date the change was made
        @type date: C{string}
        @param description: description of what the change entailed
        @type description: C{string}
        """
        self.version = version
        self.date = date
        self.description = description

def _parse_update(xml_update):
    """
    Take the C{Element} for a history update and turn it into a
    L{HistoryUpdate} object.

    @param xml_update: C{Element} for a history update
    @type xml_update: C{Element}

    @return: L{HistoryUpdate} object
    @rtype: L{HistoryUpdate}
    """
    return HistoryUpdate(xml_update.findtext('version'), 
                         xml_update.findtext('date'), 
                         xml_update.findtext('description'))

def parse_history(xml_tree):
    """
    Parse the history element in the given C{Element} tree.

    @param xml_tree: root of C{Element} tree that has history in it
    @type xml_tree: C{Element} or C{ElementTree}

    @return: C{List} of L{HistoryUpdate}s
    @rtype: C{list} of L{HistoryUpdate}
    """
    check_version(xml_tree)
    return [_parse_update(xml_update) 
            for xml_update in xml_tree.findall('history/update')]

############################################################
# TOP
############################################################

def parse_top_level(xml_tree):
    """ 
    Parse all of the simple root elements in an SABX file. 

    The simple root elements are:
      - uuid
      - version
      - zip_prefix
      - description
      - ride_type
      - title
      - description
      - terrain

    @param xml_tree: root of C{Element} tree that has SABX data
    @type xml_tree: C{Element} or C{ElementTree}

    @return: C{dict} of root elements
    @rtype: C{dict}
    """
    check_version(xml_tree)
    sabx = {}

    sabx['uuid'] = xml_tree.findtext('uuid')
    sabx['version'] = xml_tree.findtext('version')
    sabx['zip_prefix'] = xml_tree.findtext('zip_prefix')

    desc = et.tostring(xml_tree.find('description')).\
        replace("<description>", "").\
        replace("</description>", "").\
        replace("<description />", "")
    desc = desc.strip()

    sabx['ride_type'] = xml_tree.findtext('ride_type')
    sabx['title'] = xml_tree.findtext('title')
    sabx['description'] = desc
    sabx['terrain'] = xml_tree.findtext('terrain')

    return sabx

############################################################
# OVERALL
############################################################

def parse_tree(xml_tree):
    """ 
    Parse a whole SABX file. 

    @param xml_tree: root of C{Element} tree that has SABX data
    @type xml_tree: C{Element} or C{ElementTree}

    @return: C{dict} of parsed SABX data
    @rtype: C{dict}
    """
    sabx = parse_top_level(xml_tree)
    sabx['photos'] = parse_photos(xml_tree)
    sabx['park_list'], sabx['park_dict'] = parse_parking(xml_tree)
    sabx['turn_list'], sabx['turn_dict'] = parse_turns(xml_tree)
    sabx['seg_list'], sabx['seg_dict'] = parse_segments(xml_tree)
    sabx['stop_list'], sabx['stop_dict'] = parse_stops(xml_tree)
    sabx['poi_list'], sabx['poi_dict'] = parse_pois(xml_tree)
    sabx['ride_list'], sabx['ride_dict'] = parse_rides(xml_tree)
    sabx['history'] = parse_history(xml_tree)

    return sabx
