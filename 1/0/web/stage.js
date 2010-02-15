//**************************************************************************/
//
// sabx10 - an SABX file manipulation library
// Copyright (C) 2009, 2010 Jay Farrimond (jay@sabikerides.com)
//
// This file is part of sabx10.
//
// sabx10 is free software: you can redistribute it and/or modify it under the
// terms of the GNU General Public License as published by the Free Software
// Foundation, either version 3 of the License, or (at your option) any later
// version.
//
// sabx10 is distributed in the hope that it will be useful, but WITHOUT ANY
// WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
// FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
// details.
//
// You should have received a copy of the GNU General Public License along with
// sabx10.  If not, see <http://www.gnu.org/licenses/>.
//
//**************************************************************************/
var map;
var rideIndex = 0;

//****************************************************************
// DISPLAY
//****************************************************************

function centerAndZoomMap() {
    var sw = new GLatLng(ride_bounds[rideIndex].min_lat, 
			 ride_bounds[rideIndex].min_lon);
    var ne = new GLatLng(ride_bounds[rideIndex].max_lat, 
			 ride_bounds[rideIndex].max_lon);
    var bounds = new GLatLngBounds(sw, ne);
    map.setCenter(bounds.getCenter(), 
		  map.getBoundsZoomLevel(bounds));
}

function addSegments(index) {
    for( var i = 0; i < segments[index].length; i++ ) {
	var line = new GPolyline.fromEncoded(segments[index][i].polyline);
        map.addOverlay(line);
    }
}

function displayRide(index) {
    map.clearOverlays();
    centerAndZoomMap();
    addSegments(index);
}

//****************************************************************
// LAYOUT
//****************************************************************

// I'm assuming nothing has a margin.

var spacing = 5;
var showTabs = true;

function setItemHeight(item, availHeight) {
    var height = availHeight -
	parseInt(item.css("padding-top"), 10) -
	parseInt(item.css("padding-bottom"), 10) -
	parseInt(item.css("border-top-width"), 10) -
	parseInt(item.css("border-bottom-width"), 10);
    item.height(height);
    return height;
}

function setItemWidth(item, availWidth) {
    var width = availWidth -
	parseInt(item.css("padding-left"), 10) -
	parseInt(item.css("padding-right"), 10) -
	parseInt(item.css("border-left-width"), 10) -
	parseInt(item.css("border-right-width"), 10);
    item.width(width);
    return width;
}

function setItemPosition(item, top, left) {
    item.css("top", top ); 
    item.css("left", left );
}

function layoutHeader(winWidth) {
    var hdr = $("#header");
    setItemPosition(hdr, spacing, spacing);
    setItemWidth(hdr, winWidth - (spacing * 2) );
    return hdr.outerHeight(true) + spacing;
}

function layoutCopyright(winHeight, winWidth) {
    var cpy = $("#sab-copyright");
    setItemPosition(cpy, winHeight - cpy.outerHeight(true) - spacing, spacing);
    setItemWidth(cpy, winWidth - (spacing * 2) );
    return cpy.outerHeight(true) + spacing;
}

function layoutMap(winHeight, hdrBottom, tabsRight) {
    var map = $("#map");
    setItemPosition(map, hdrBottom + spacing + 1, tabsRight + spacing + 1);

    var divAvailHeight = winHeight - (hdrBottom + 1) - (spacing * 2);
    divAvailHeight = setItemHeight(map, divAvailHeight);

    var mapAvailHeight = divAvailHeight - $("#map-toggles").outerHeight(true);
    setItemHeight($("#map-canvas"), mapAvailHeight);

    var mapAvailWidth = $(window).width() - (tabsRight + 1) - (spacing * 2);
    mapAvailWidth = setItemWidth($("#map"), mapAvailWidth);
    setItemWidth($("#map-canvas"), mapAvailWidth);
}

function layoutEverything() {
    var windowHeight = $(window).height();
    var windowWidth = $(window).width();

    var headerBottom = layoutHeader(windowWidth);
    var copyHeight = layoutCopyright(windowHeight, windowWidth);
    windowHeight -= copyHeight;
    layoutMap(windowHeight, headerBottom, -1);
}

//****************************************************************
// SETUP
//****************************************************************

function initializeMap() {
    map = new GMap2(document.getElementById("map-canvas"));
    if( ride_data.ride_type == "mtb" ) {
	map.setMapType(G_PHYSICAL_MAP);
    }
    map.setUIToDefault();
    centerAndZoomMap(); // redundant, but have to before calling ops on map
}

$(document).ready(function() {
	if (GBrowserIsCompatible()) {
	    $("#no_js_warning").css("display", "none");
	    $("html,body").css("overflow", "hidden");
	    $("#header,#map,#sab-copyright").css("display", "block");
	    $("#header,#map,#sab-copyright").css("position", "absolute");
	    layoutEverything();
	    initializeMap();
	    displayRide(rideIndex);

	    $(document.body).unload(function() {
		    GUnload();
		});

	    $(window).resize(function() {
		    layoutEverything();
		    map.checkResize();
		});
 
	    //************************
	    // misc. user interaction
	    //************************

	    function unSelClass(theClass) {
		$(theClass).removeClass("header-ride-sel");
		$(theClass).addClass("header-ride-unsel");
	    }

	    function selClass(theClass) {
		$(theClass).removeClass("header-ride-unsel");
		$(theClass).addClass("header-ride-sel");
	    }

	    for( var i=0; i<ride_data.ride_count; i++) {
		var label = '.header-ride-' + i;
		$(label).data("index", i).click(function(event) {
			unSelClass(".header-ride-" + rideIndex);
			rideIndex = $(event.target).data("index");
			selClass(".header-ride-" + rideIndex);
			displayRide(rideIndex);
			event.preventDefault();
		    });
	    }

	    $("#map-rezoom").click(function(event) {
		    centerAndZoomMap();
		    event.preventDefault();
		});

	}
    });
