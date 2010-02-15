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
Handle merging CSV files into SABX files.
"""

import csv
import sys

from sabx10.oxm import Point, Ride, Parking, Turn, Segment, Stop, Poi
from sabx10.templating import SabxProcessor

class BadPointError(Exception):
    """
    This is raised when the CsvProcessor._process_lat_lon function can't
    interpret a point passed to it.
    """
    pass

class CsvProcessor(SabxProcessor):
    """
    Merge an SABX 1.0 file and a CSV file. Process it through an SABX 1.0
    template and output it into a SABX 1.0 file.
    """

    def __init__(self, template_file=None, man=None):
        """
        Adds the id, csv, and generate options to the standard SABX 1.0
        template processor.

        @param template_file: (optional) file name of template file
        @type template_file: C{string}
        @param man: (optional) extended program help
        @type man: C{string}
        """
        SabxProcessor.__init__(self, template_file, man)

        self.parser.usage = "%s csv_file" % self.parser.usage
        self.parser.add_option("-d", "--id", dest="id",
                               help="id of segment to merge into", 
                               default="1", metavar="ID")
        self.parser.add_option("-b", "--blank", dest="blank",
                               action="store_true",
                               help="generate a blank CSV file", 
                               default=False, metavar="BLANK")

    def _generate_blank(self):
        csv = open(self.csv, "w")
        csv.write("TYPE,START POINT,END POINT,TURN COMMENTS,TURN CUE,"
                  "ROAD,ROAD COMMENTS,LANES,SHOULDER,SPEED,TRAFFIC\n")
        csv.close()

    def process_options(self):
        """
        Get the CSV file name.  It's expected to be the last command-line
        argument.  Print a blank CSV file and exit if asked to.
        """
        SabxProcessor.process_options(self, 1)
        self.csv = self.args[-1]

        if self.options.blank:
            self._generate_blank()
            sys.exit(0)

    def _process_lat_lon(self, lat, lon):
        """
        Get the lat, lon, and waypoint corresponding to the lat and lon values
        passed in.  If lat contains a point id, then the corresponding point is
        found.  Otherwise, the point closest to (lat, lon) is found.

        @raises: L{BadPointError}

        @param lat: latitude or point to search for
        @type lat: C{string}
        @param lon: longitude to search for
        @type lon: C{string}
        """
        waypoint = None
        if lat.find('.') == -1:
            for pt in self.template_data['seg_dict'][self.options.id].waypoints:
                if pt.id == lat:
                    waypoint = pt
                    lat = pt.lat
                    lon = pt.lon
                    break
            else:
                raise BadPointError(
                    "Matching point for '%s' not found!" % lat)
        else:
            dist = 100000.0
            check_pt = Point(lat, lon)
            for pt in self.template_data['seg_dict'][self.options.id].waypoints:
                t_dist = check_pt.calculate_distance(pt)
                if t_dist < dist:
                    waypoint = pt
                    dist = t_dist

        return lat, lon, waypoint

    def _parse_parking(self, id, item):
        """
        Parse the CSV line as if it's a PARK item.

        @raises: L{BadPointError}

        @param id: id for this item
        @type id: C{int}
        @param item: CSV line item to parse
        @type item: C{dict}
        """
        try:
            lat, lon, wypt = self._process_lat_lon(item['START POINT'], 
                                                   item['END POINT'])
        except BadPointError as bpe:
            raise BadPointError("Bad parking point: %s" % bpe)
    
        return Parking(str(id), item['ROAD'], lat, lon)

    def _parse_turn(self, id, fromto, seg):
        """
        Parse the CSV line as if it's a ROAD item, and remove the turn data 
        from it.

        @param id: id for this item
        @type id: C{int}
        @param fromto: fromto part of the turn
        @type fromto: C{string}
        @param seg: CSV ROAD item to parse
        @type seg: C{dict}
        """
        return Turn(str(id), "%s to %s" % (fromto, seg['ROAD']),
                    "%s %s" % (seg['TURN CUE'], seg['ROAD']),
                    seg['TURN COMMENTS'])

    def _get_segment_waypoints(self, seg):
        """
        Get the waypoints for the corresponding segment.  These are the points
        from START POINT to END POINT.

        @param seg: segment to get points for
        @type seg: SABX 1.0 L{Segment}
        """
        seg_pts = []
        in_pts = False
        for pt in self.template_data['seg_dict'][self.options.id].waypoints:
            if pt.id == seg['START POINT']:
                in_pts = True

            if in_pts:
                seg_pts.append(pt)

            if pt.id == seg['END POINT']:
                in_pts = False

        return seg_pts

    def _parse_segment(self, id, fromto, seg):
        """
        Parse the CSV line as if it's a ROAD item, and remove the segment data 
        from it.

        @param id: id for this item
        @type id: C{int}
        @param fromto: fromto part of the turn
        @type fromto: C{string}
        @param seg: CSV ROAD item to parse
        @type seg: C{dict}
        """
        return Segment(str(id), seg['ROAD'], fromto, seg['ROAD COMMENTS'],
                       seg['LANES'], seg['SHOULDER'], seg['TRAFFIC'], 
                       seg['SPEED'], self._get_segment_waypoints(seg))

    def _update_segment_fromto(self, seg, tofrom):
        """
        Update the fromto field in a segment.

        @param seg: segment to update
        @type seg: SABX 1.0 L{Segment}
        @param tofrom: value to update with
        @type tofrom: C{string}
        """
        seg.fromto = "%s to %s" % (seg.fromto, tofrom)

    def _parse_stop(self, id, item):
        """
        Parse the CSV line as if it's a STOP item.

        @raises: L{BadPointError}

        @param id: id for this item
        @type id: C{int}
        @param item: CSV line item to parse
        @type item: C{dict}
        """
        try:
            lat, lon, wypt = self._process_lat_lon(item['START POINT'], 
                                                   item['END POINT'])
        except BadPointError as bpe:
            raise BadPointError("Bad stop point: %s" % bpe)

        if wypt.stop is None:
            wypt.stop = str(id)
        else:
            wypt.stop = "%s,%s" % (wypt.stop, str(id))
        return Stop(str(id), item['TURN CUE'], item['ROAD'], lat, lon)

    def _parse_poi(self, id, item):
        """
        Parse the CSV line as if it's a POI item.

        @raises: L{BadPointError}

        @param id: id for this item
        @type id: C{int}
        @param item: CSV line item to parse
        @type item: C{dict}
        """
        try:
            lat, lon, wypt = self._process_lat_lon(item['START POINT'], 
                                                   item['END POINT'])
        except BadPointError as bpe:
            raise BadPointError("Bad poi point: %s" % bpe)

        if wypt.poi is None:
            wypt.poi = str(id)
        else:
            wypt.poi = "%s,%s" % (wypt.poi, str(id))
        return Poi(str(id), item['ROAD'], lat, lon)

    def _parse_csv(self):
        """
        Parse the CSV file and merge it with the SABX 1.0 template data.
        """
        new_sabx = {}
        new_sabx['park_list'] = []
        new_sabx['park_dict'] = {}

        new_sabx['turn_list'] = []
        new_sabx['turn_dict'] = {}

        new_sabx['seg_list'] = []
        new_sabx['seg_dict'] = {}

        new_sabx['stop_list'] = []
        new_sabx['stop_dict'] = {}

        new_sabx['poi_list'] = []
        new_sabx['poi_dict'] = {}

        new_ride = Ride('1', '', '', [], [])
        new_sabx['ride_list'] = [new_ride]
        new_sabx['ride_dict'] = {'1': new_ride}

        fromto = "parking"
        prev_seg = None

        # TYPE, START POINT, END POINT, TURN COMMENTS, TURN CUE, 
        # ROAD, ROAD COMMENTS, LANES, SHOULDER, SPEED, TRAFFIC
        for index, row in enumerate(
            csv.DictReader(open(self.csv)), start=1):

            # ride
            if row['TYPE'] == 'RIDE':
                new_ride.description = row['ROAD']

            # parking
            if row['TYPE'] == 'PARK':
                new_parking = self._parse_parking(index, row)
                new_sabx['park_list'].append(new_parking)
                new_sabx['park_dict'][new_parking.id] = new_parking
                new_ride.parking = new_parking.id

            # road
            elif row['TYPE'] == 'ROAD':
                new_turn = self._parse_turn(index, fromto, row)
                new_sabx['turn_list'].append(new_turn)
                new_sabx['turn_dict'][new_turn.id] = new_turn
                new_ride.turns.append(new_turn.id)

                new_seg = self._parse_segment(index, fromto, row)
                new_sabx['seg_list'].append(new_seg)
                new_sabx['seg_dict'][new_seg.id] = new_seg
                new_ride.segs.append(new_seg.id)

                fromto = new_seg.road
                if prev_seg:
                    self._update_segment_fromto(prev_seg, fromto)
                prev_seg = new_seg

            # stop
            elif row['TYPE'] == 'STOP':
                new_stop = self._parse_stop(index, row)
                new_sabx['stop_list'].append(new_stop)
                new_sabx['stop_dict'][new_stop.id] = new_stop

            # poi
            elif row['TYPE'] == 'POI':
                new_poi = self._parse_poi(index, row)
                new_sabx['poi_list'].append(new_poi)
                new_sabx['poi_dict'][new_poi.id] = new_poi

        return new_sabx

    def get_template_data(self):
        """
        Update the template data by merging it with the specified CSV data.
        """
        SabxProcessor.get_template_data(self)
        new_sabx = self._parse_csv()
        self.template_data['park_list'], self.template_data['park_dict'] = \
            new_sabx['park_list'], new_sabx['park_dict']
        self.template_data['turn_list'], self.template_data['turn_dict'] = \
            new_sabx['turn_list'], new_sabx['turn_dict']
        self.template_data['seg_list'], self.template_data['seg_dict'] = \
            new_sabx['seg_list'], new_sabx['seg_dict']
        self.template_data['stop_list'], self.template_data['stop_dict'] = \
            new_sabx['stop_list'], new_sabx['stop_dict']
        self.template_data['poi_list'], self.template_data['poi_dict'] = \
            new_sabx['poi_list'], new_sabx['poi_dict']
        self.template_data['ride_list'], self.template_data['ride_dict'] = \
            new_sabx['ride_list'], new_sabx['ride_dict']
