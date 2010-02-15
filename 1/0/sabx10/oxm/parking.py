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
Parking place handling.
"""
from geom import Point
from utils import get_from_id

############################################################
# XML
############################################################

class Parking(Point):
    """
    A C{Parking} object sub-classes L{Point} and adds a description to describe
    a parking place.

    @ivar description: description of the parking place
    @type description: C{string}
    """
    def __init__(self, id, description, lat, lon):
        """
        Save the passed-in data.

        @param id: id of the parking place
        @type id: C{string}
        @param description: description of the parking place
        @type description: C{string}
        @param lat: latitude of parking place
        @type lat: C{float}
        @param lon: longitude of parking place
        @type lon: C{float}
        """
        Point.__init__(self, lat, lon, id=id)
        self.description = description

def _parse_parking_xml(xml_parking):
    """
    Take the C{Element} for a parking place and turn it into a L{Parking}
    object.

    @param xml_parking: C{Element} for a parking place
    @type xml_parking: C{Element}

    @return: L{Parking} object
    @rtype: L{Parking}
    """
    return Parking(id = xml_parking.attrib['id'],
                   description = xml_parking.findtext('description'),
                   lat = xml_parking.findtext('lat'),
                   lon = xml_parking.findtext('lon'))

def parse_parking(xml_tree):
    """
    Get all the parking place elements in the given C{Element} tree and create
    a list of them with L{Parking} objects.

    @param xml_tree: root of C{Element} tree that has parking places in it
    @type xml_tree: C{Element} or C{ElementTree}

    @return: parking places in a list and a dictionary
    @rtype: (C{list},C{dict}) of L{Parking}
    """
    xml_parking_places = xml_tree.findall('parking')
    parking_list = []
    parking_dict = {}
    for xml_parking in xml_parking_places:
        new_parking = _parse_parking_xml(xml_parking)
        parking_list.append(new_parking)
        parking_dict[new_parking.id] = new_parking

    return parking_list, parking_dict

############################################################
# RIDES
############################################################

def process_ride_parking(xml_ride, xml_parking_places):
    """
    Process the parking place reference for the give ride and generate a full
    L{Parking} object for it.

    @param xml_ride: root of C{Element} tree for this ride
    @type xml_ride: C{Element}
    @param xml_parking_places: C{list} of C{Element} trees for parking places
    @type xml_parking_places: C{list} of C{Element} trees

    @return: L{Parking} object for the ride
    @rtype: L{Parking}
    """
    xml_ride_parking = xml_ride.find('parking_ref')
    xml_parking = get_from_id(xml_parking_places, xml_ride_parking.attrib['id'])
    ret = _parse_parking_xml(xml_parking)
    ret.description = " ".join(ret.description.split())
    return ret
