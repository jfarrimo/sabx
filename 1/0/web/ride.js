//**************************************************************************
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
//**************************************************************************
var map;
var rideIndex = 0;

//****************************************************************
// MARKERS
//****************************************************************

var mgr = null;
var parkingMarker = null;
var stopMarkers = null;
var poiMarkers = null;
var turnMarkers = null;

function createParkingOptions(position) {
    var icon = new google.maps.MarkerImage("../markers/park.png", 
					   google.maps.Size(32, 32));
    return { icon: icon, position: position, title: "Parking" };
}

function createStopOptions(position) {
    var icon = new google.maps.MarkerImage("../markers/stop.png", 
					   google.maps.Size(32, 32));
    return { icon: icon, position: position, title: "Stop" };
}

function createPOIOptions(position) {
    var icon = new google.maps.MarkerImage("../markers/poi.png", 
					   google.maps.Size(32, 32));
    return { icon: icon, position: position, title: "POI" };
}

function createTurnOptions(icon_name, position) {
    var icon = new google.maps.MarkerImage(icon_name,
					   google.maps.Size(32, 32));
    return { icon: icon, position: position, title: "Turn" };
}

function createMarker(map, options, z, theHtml) {
    var marker = new google.maps.Marker(options);
    google.maps.event.addListener(marker, "click", function() {
	    infoWindow.setContent(theHtml);
	    infoWindow.open(map,marker);
	});
    options.zIndexProcess = function() {
        return z;
    };
    return marker;
}

function createParkingIcon(index, map) {
    var point = new google.maps.LatLng(parking[index].lat, 
				       parking[index].lon);
    var parkingOptions = createParkingOptions(point);
    parkingMarker = createMarker(map, parkingOptions, 
				 1000, parking[index].html);
}

function createStopIcons(index, map) {
    stopMarkers = [];
    for (var i = 0; i < stops[index].length; i++) {
	var point = new google.maps.LatLng(stops[index][i].lat, 
					   stops[index][i].lon);
	var stopOptions = createStopOptions(point);
	var marker = createMarker(map, stopOptions, 750 + i, 
				  stops[index][i].html);
	stopMarkers.push(marker);
    }
}

function createPOIIcons(index, map) {
    poiMarkers = [];
    for (var i = 0; i < pois[index].length; i++) {
	var point = new google.maps.LatLng(pois[index][i].lat, 
					   pois[index][i].lon);
	var poiOptions = createPOIOptions(point);
	var marker = createMarker(map, poiOptions, 750 + i, 
				  pois[index][i].html);
	poiMarkers.push(marker);
    }
}

function createTurnIcons(index, map) {
    turnMarkers = [];
    for (var i = 0; i < turns[index].length; i++) {
	var point = new google.maps.LatLng(turns[index][i].lat, turns[index][i].lon);
	var turnOptions = 
	    createTurnOptions("../markers/" + turns[index][i].icon, point);
	var marker = createMarker(map, turnOptions, 100 + i, 
				  turns[index][i].html);
	turnMarkers.push(marker);
    }
}

function createMarkers(index, map) {
    createParkingIcon(index, map);
    createStopIcons(index, map);
    createPOIIcons(index, map);
    createTurnIcons(index, map);
}

function destroyMarkers() {
    parkingMarker = null;
    stopMarkers = null;
    poiMarkers = null;
    turnMarkers = null;
}

function hideMarkers() {
    if (mgr !== null) {
	mgr.clearMarkers();
    }

    if (parkingMarker !== null) {
	parkingMarker.setMap(null);
    }
    if (stopMarkers !== null) {
	for (i=0; i<stopMarkers.length; i++) {
	    stopMarkers[i].setMap(null);
	}
    }
    if (poiMarkers !== null) {
	for (i=0; i<poiMarkers.length; i++) {
	    poiMarkers[i].setMap(null);
	}
    }
    if (turnMarkers !== null) {
	for (i=0; i<turnMarkers.length; i++) {
	    turnMarkers[i].setMap(null);
	}
    }
}

function showMarkers(map) {
    if (mgr !== null) {
	mgr.clearMarkers();
    }

    parkingMarker.setMap(map);
    for (i=0; i<stopMarkers.length; i++) {
	stopMarkers[i].setMap(map);
    }
    for (i=0; i<poiMarkers.length; i++) {
	poiMarkers[i].setMap(map);
    }
    for (i=0; i<turnMarkers.length; i++) {
	turnMarkers[i].setMap(map);
    }
}

function clusterMarkers(map) {
    mgr.addMarker(parkingMarker);
    for (i=0; i<stopMarkers.length; i++) {
	mgr.addMarker(stopMarkers[i]);
    }
    for (i=0; i<poiMarkers.length; i++) {
	mgr.addMarker(poiMarkers[i]);
    }
    for (i=0; i<turnMarkers.length; i++) {
	mgr.addMarker(turnMarkers[i]);
    }
}

function addMarkers(index, map) {
    createMarkers(index, map);
    if ( $("#cluster-markers").get(0).checked ) {
	clusterMarkers(map);
    }
    else {
	showMarkers(map);
    }
}

//****************************************************************
// OVERLAYS
//****************************************************************

var segLines = null;
var infoWindow = new google.maps.InfoWindow({content: "", maxWidth: 350});

function createSegmentPolyline(map, polyline, theHtml) {
    var pt_array = [];
    for (i=0; i<polyline.pts.length; i++) {
	pt_array.push(new google.maps.LatLng(polyline.pts[i][0], 
					     polyline.pts[i][1]));
    }
    polyline.path = pt_array;
    
    var line = new google.maps.Polyline(polyline);
    google.maps.event.addListener(line, "click", function(event) {
	    infoWindow.setContent(theHtml);
	    infoWindow.setPosition(event.latLng);
	    infoWindow.open(map);
	});
	  
    return line;
}

function addSegments(index, map) {
    segLines = [];
    for( var i = 0; i < segments[index].length; i++ ) {
	var seg = createSegmentPolyline(map, 
					segments[index][i].polyline, 
					segments[index][i].theHtml);
	seg.setMap(map);
	segLines.push(seg);
    }
}

function clearSegments() {
    if (segLines !== null ) {
	for (i=0; i<segLines.length; i++) {
	    segLines[i].setMap(null);
	}
	segLines = null;
    }
}

function clearOverlays(){
    hideMarkers();
    destroyMarkers();
    clearSegments();
}

//****************************************************************
// PARKING DIRECTIONS
//****************************************************************

function printableParkingDirections(index) {
    var dirUrl = "http://maps.google.com/maps?" + 
	//"saddr=" + $("#park-from").get(0).value.replace(/[ \n]/g, "+") +
	"&daddr=" + parking[index].lat + "," + parking[index].lon;
    window.open(dirUrl);
}

//****************************************************************
// DISPLAY
//****************************************************************

function getBounds() {
    var sw = new google.maps.LatLng(ride_bounds[rideIndex].min_lat, 
			 ride_bounds[rideIndex].min_lon);
    var ne = new google.maps.LatLng(ride_bounds[rideIndex].max_lat, 
			 ride_bounds[rideIndex].max_lon);
    return new google.maps.LatLngBounds(sw, ne);
}

function centerAndZoomMap() {
    var bounds = getBounds();
    map.fitBounds(bounds);
    //addParkingDirectionsBounds(bounds);
    //map.setCenter(bounds.getCenter(), map.getBoundsZoomLevel(bounds));
}

function displayParking(index) {
    $(".parking-spans").hide();
    $("#parking-" + index).show();
}

function displayInstructions(index) {
    $(".inst-tabs").hide();
    if( $("#inst-ckbox-ck").get(0).checked ) {
	$("#inst-long-"+index).show();
    } else {
	$("#inst-short-"+index).show();
    }
}

function displayProfiles(index) {
    $(".prof-tabs").hide();
    $(".prof-" + index).show();
}

function displayStops(index) {
    $(".stops-tabs").hide();
    $("#stops-" + index).show();
}

function displayPOIs(index) {
    $(".pois-tabs").hide();
    $("#pois-" + index).show();
}

function displayRide(index) {
    //clearParkingDirections();
    clearOverlays();
    centerAndZoomMap();
    
    addMarkers(index, map);
    addSegments(index, map);

    displayParking(index);
    displayInstructions(index);
    displayProfiles(index);
    displayStops(index);
    displayPOIs(index);
}

function resizeMapDiv(map) {
    google.maps.event.trigger(map, 'resize')
}

//****************************************************************
// LAYOUT
//****************************************************************

// I'm assuming nothing has a margin.

var spacing = 0;

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

function layoutTabs(winHeight, winWidth, hdrBottom) {
    var tabs = $("#tabs");
    setItemPosition(tabs, hdrBottom + spacing + 1, spacing);

    var divAvailHeight = winHeight - (hdrBottom + 1) - (spacing * 2);
    setItemHeight(tabs, divAvailHeight);
    var tabWidth = Math.min(500, winWidth / 3);
    tabWidth = Math.max(350, tabWidth);
    setItemWidth(tabs, tabWidth);

    var tabsAvailHeight = divAvailHeight - $(".ui-tabs-nav").outerHeight();
    setItemHeight($("#tabs-overview"), tabsAvailHeight);
    setItemHeight($("#tabs-parking"), tabsAvailHeight);
    setItemHeight($("#tabs-stops"), tabsAvailHeight);
    setItemHeight($("#tabs-instructions"), tabsAvailHeight);
    setItemHeight($("#tabs-profiles"), tabsAvailHeight);

    return tabs.outerWidth() + spacing - 1;
}

function layoutMap(winHeight, hdrBottom, tabsRight) {
    var map = $("#map");
    setItemPosition(map, hdrBottom + spacing + 1, tabsRight + spacing + 1);

    var mapAvailHeight = winHeight - (hdrBottom + 1) - (spacing * 2);
    divAvailHeight = setItemHeight(map, mapAvailHeight);

    var mapAvailWidth = $(window).width() - (tabsRight + 1) - (spacing * 2);
    mapAvailWidth = setItemWidth($("#map"), mapAvailWidth);
}

function layoutEverything() {
    var windowHeight = $(window).height();
    var windowWidth = $(window).width();

    var headerBottom = layoutHeader(windowWidth) - 1;
    if ( $("#show-tabs").get(0).checked ) {
	var tabsRight = layoutTabs(windowHeight, windowWidth, headerBottom);
	layoutMap(windowHeight, headerBottom, tabsRight);
    }
    else {
	layoutMap(windowHeight, headerBottom, -1);
    }
}

//****************************************************************
// SETUP
//****************************************************************

function initializeMap() {
    var bounds = getBounds();

    var map_type = google.maps.MapTypeId.ROADMAP;
    if( ride_data.ride_type == "mtb" ) {
	map_type = google.maps.MapTypeId.TERRAIN;
    }

    var myOptions = {
	zoom: 8,
	center: bounds.getCenter(),
	mapTypeId: map_type
    };

    map = new google.maps.Map(document.getElementById("map-canvas"), 
			      myOptions);

    //initParkingDirections();
    //addParkingDirectionsBounds(bounds);
    map.fitBounds(bounds);

    mgr = new MarkerClusterer(map, [], {gridSize: 35});

    

    /* turn off map adds since they suck
    var publisher_id = 'pub-3294694121856190';
    var adsManagerOptions = {
	maxAdsOnMap : 2,
	style: 'adunit'
    };
    adsManager = new GAdsManager(map, publisher_id, adsManagerOptions);
    adsManager.enable();
    */
}

$(document).ready(function() {
	$("#no_js_warning").css("display", "none");
	$("html,body").css("overflow", "hidden");
	$("#header,#tabs,#map").css("display", "block");
	$("#header,#tabs,#map").css("position", "absolute");
	$("#tabs").tabs();
	$(".prof-dialogs").dialog({ autoOpen: false, 
		    height: 450, 
		    width: 800 });
	$(".help-dialogs").dialog({ autoOpen: false, 
		    height: 450, 
		    width: 800 });
	$(".sabx_button").button();
	$("#ride-distances").buttonset();
	layoutEverything();
	initializeMap();
	displayRide(rideIndex);

	$(document.body).unload(function() {
		GUnload();
	    });

	$(window).resize(function() {
		layoutEverything();
		resizeMapDiv(map);
		centerAndZoomMap();
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

	$('#header-ride-0').get(0).checked = true;
	$('#over-ride-0').get(0).checked = true;
	for( var i=0; i<ride_data.ride_count; i++) {
	    var label = '#header-ride-' + i;
	    $(label).data("index", i).click(function(event) {
		    rideIndex = $(event.target).data("index");
		    //clearParkingDirections();
		    displayRide(rideIndex);
		    $('#over-ride-' + rideIndex).get(0).checked = true;
		});
	    var label = '#over-ride-' + i;
	    $(label).data("index", i).click(function(event) {
		    rideIndex = $(event.target).data("index");
		    //clearParkingDirections();
		    displayRide(rideIndex);
		    $('#header-ride-' + rideIndex).get(0).checked = true;
		});
	}

	$(".parking-spans").click(function(event) {
		var parts = event.target.id.split('-');
		var ride = parseInt(parts[1], 10);
		var point = 
		    new google.maps.LatLng(parking[ride].lat, 
					   parking[ride].lon);
		infoWindow.setContent(parking[ride].html);
		infoWindow.setPosition(point);
		infoWindow.open(map);
	    });

	//*********************
	// stops
	//*********************
	$(".stops-rows").click(function(event) {
		var classes = event.target.className.split(' ');
		var parts = classes[0].split('-');
		var ride = parseInt(parts[1], 10);
		var index = parseInt(parts[2], 10);
		var point = 
		    new google.maps.LatLng(stops[ride][index].lat, 
					   stops[ride][index].lon);
		infoWindow.setContent(stops[ride][index].html);
		infoWindow.setPosition(point);
		infoWindow.open(map);
	    });

	//*********************
	// pois
	//*********************
	$(".pois-rows").click(function(event) {
		var classes = event.target.className.split(' ');
		var parts = classes[0].split('-');
		var ride = parseInt(parts[1], 10);
		var index = parseInt(parts[2], 10);
		var point = 
		    new google.maps.LatLng(pois[ride][index].lat, 
					   pois[ride][index].lon);
		infoWindow.setContent(pois[ride][index].html);
		infoWindow.setPosition(point);
		infoWindow.open(map);
	    });

	//*********************
	// instructions
	//*********************
	$(".inst-ckbox").click(function() {
		displayInstructions(rideIndex);
	    });
	$(".inst-rows").click(function(event) {
		var parts = event.target.className.split('-');
		var ride = parseInt(parts[1], 10);
		var index = parseInt(parts[2], 10);
		var point;
		if( parts[0] == "segs" ) {
		    point = 
			new google.maps.LatLng(segments[ride][index].mid_lat, 
					       segments[ride][index].mid_lon);
		    infoWindow.setContent(segments[ride][index].theHtml);
		    infoWindow.setPosition(point);
		    infoWindow.open(map);
		}
		else {
		    point = 
			new google.maps.LatLng(turns[ride][index].lat, 
					       turns[ride][index].lon);
		    infoWindow.setContent(turns[ride][index].html);
		    infoWindow.setPosition(point);
		    infoWindow.open(map);
		}
	    });

	//*********************
	// profiles
	//*********************
	$(".prof-rows").click(function(event) {
		if( event.target.className.indexOf("prof-graph") == -1 ){
		    var classes = event.target.className.split(' ');
		    var parts = classes[0].split('-');
		    var ride = parseInt(parts[1], 10);
		    var index = parseInt(parts[2], 10);
		    var point = 
			new google.maps.LatLng(segments[ride][index].mid_lat, 
					       segments[ride][index].mid_lon);
		    infoWindow.setContent(segments[ride][index].theHtml);
		    infoWindow.setPosition(point);
		    infoWindow.open(map);
		}
	    });
	$(".prof-graph-prof").click(function(event) {
		var dlgName = "";
		if( event.target.className.indexOf("prof-graph-prof") > -1 ){
		    dlgName = "#prof-prof-";
		} else {
		    dlgName = "#prof-hist-";
		}
		var classes = event.target.className.split(' ');
		var parts = classes[0].split('-');
		var ride = parseInt(parts[1], 10);
		if( parts.length > 2 ) {
		    var index = parseInt(parts[2], 10);
		    dlgName = dlgName + ride + "-" + index;
		} else {
		    dlgName = dlgName + ride;
		}
		$(dlgName).dialog('open');
	    });

	//*********************
	// map controls
	//*********************
	$("#show-tabs").click(function(event) {
		if ( $("#show-tabs").get(0).checked ) {
		    $("#tabs").show();
		}
		else {
		    $("#tabs").hide();
		}

		layoutEverything();
		resizeMapDiv(map);
		centerAndZoomMap();
	    });
	$("#cluster-markers").click(function(event) {
		hideMarkers();
		destroyMarkers();
		addMarkers(rideIndex, map);
	    });
	$("#map-rezoom").click(function(event) {
		centerAndZoomMap();
		event.preventDefault();
	    });

	//********************
	// parking directions
	//********************

	$("#park-print").click(function(event) {
		var dirUrl = "http://maps.google.com/maps?" + 
		    "&daddr=" + parking[rideIndex].lat + "," + parking[rideIndex].lon;
		window.open(dirUrl);
		event.preventDefault();
	    });

	//********************
	// help
	//********************
	$("#parking-help").click(function(event) {
		$("#help-dlg-parking").dialog('open');
		event.preventDefault();
	    });
	$("#stops-help").click(function(event) {
		$("#help-dlg-stops").dialog('open');
		event.preventDefault();
	    });
	$("#pois-help").click(function(event) {
		$("#help-dlg-pois").dialog('open');
		event.preventDefault();
	    });
	$("#inst-help").click(function(event) {
		$("#help-dlg-inst").dialog('open');
		event.preventDefault();
	    });
	$("#profs-help").click(function(event) {
		$("#help-dlg-profs").dialog('open');
		event.preventDefault();
	    });

	//********************
	// printing
	//********************
	$("#pdf-it").click(function(event) {
		var pdf = ride_data.filebase + "_" + rideIndex + ".pdf"
		    window.open(pdf);
		event.preventDefault();
	    });
    });
