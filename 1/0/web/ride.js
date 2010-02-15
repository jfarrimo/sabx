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
var mgr;
var rideIndex = 0;

//****************************************************************
// OVERLAYS
//****************************************************************

var parkingMarker = null;
var stopMarkers = null;
var poiMarkers = null;
var hasTurnIcons = true;
var infoOptions = {maxWidth: 350};

function createParkingOptions() {
    var icon = new GIcon(G_DEFAULT_ICON);
    icon.image = "../markers/park.png";
    icon.iconSize = GSize(32, 32);
    return { icon:icon, title:"Parking" };
}

function createStopOptions() {
    var icon = new GIcon(G_DEFAULT_ICON);
    icon.image = "../markers/stop.png";
    icon.iconSize = GSize(32, 32);
    return { icon:icon, title:"Stop" };
}

function createPOIOptions() {
    var icon = new GIcon(G_DEFAULT_ICON);
    icon.image = "../markers/poi.png";
    icon.iconSize = GSize(32, 32);
    return { icon:icon, title:"POI" };
}

function createTurnOptions(icon_name) {
    var icon = new GIcon(G_DEFAULT_ICON);
    icon.image = icon_name;
    icon.iconSize = GSize(32, 32);
    return { icon:icon, title:"Turn" };
}

function createMarker(map, point, options, z, theHtml) {
    var marker = new GMarker(point, options);
    GEvent.addListener(marker, "click", function() {
	    map.openInfoWindowHtml(point, theHtml, infoOptions);
	});
    options.zIndexProcess = function() {
        return z;
    };
    return marker;
}

function createSegmentPolyline(map, polyline, 
			       roadHtml, turnHtml, profileHtml) {
    var line = new GPolyline.fromEncoded(polyline);
    GEvent.addListener(line, "click", function(latlng) {
	    var roadTab = new GInfoWindowTab("Road", roadHtml);
	    var profileTab = new GInfoWindowTab("Profile", profileHtml);
	    map.openInfoWindowTabsHtml(latlng, [roadTab, profileTab], 
				       infoOptions);
	});
    return line;
}

function addParkingIcon(index) {
    if( $("#show-park-ck").get(0).checked ) {
	var parkingOptions = createParkingOptions();
	var point = new GLatLng(parking[index].lat, parking[index].lon);
	parkingMarker = createMarker(map, point, parkingOptions, 
				     1000, parking[index].html);
	map.addOverlay(parkingMarker);
    }
}

function toggleParkingIcon(index) {
    if( parkingMarker === null ) {
	addParkingIcon(index);
    } else if( parkingMarker !== null ) {
	map.removeOverlay(parkingMarker);
	parkingMarker = null;
    }
}

function addStopIcons(index) {
    if( $("#show-stops-ck").get(0).checked ) {
	stopMarkers = [];
	var stopOptions = createStopOptions();
	for (var i = 0; i < stops[index].length; i++) {
	    var point = new GLatLng(stops[index][i].lat, stops[index][i].lon);
	    var marker = createMarker(map, point, stopOptions, 750 + i, 
				      stops[index][i].html);
	    map.addOverlay(marker);
	    stopMarkers.push(marker);
	}
    }
}

function toggleStopIcons(index) {
    if( stopMarkers === null ) {
	addStopIcons(index);
    } else {
	for(i=0; i<stopMarkers.length; i++) {
	    map.removeOverlay(stopMarkers[i]);
	}
	stopMarkers = null;
    }
}

function addPOIIcons(index) {
    if( $("#show-pois-ck").get(0).checked ) {
	poiMarkers = [];
	var poiOptions = createPOIOptions();
	for (var i = 0; i < pois[index].length; i++) {
	    var point = new GLatLng(pois[index][i].lat, pois[index][i].lon);
	    var marker = createMarker(map, point, poiOptions, 750 + i, 
				      pois[index][i].html);
	    map.addOverlay(marker);
	    poiMarkers.push(marker);
	}
    }
}

function togglePOIIcons(index) {
    if( poiMarkers === null ) {
	addPOIIcons(index);
    } else {
	for(i=0; i<poiMarkers.length; i++) {
	    map.removeOverlay(poiMarkers[i]);
	}
	poiMarkers = null;
    }
}

function addTurnIcons(index) {
    if( $("#show-turns-ck").get(0).checked ) {
	mgr.clearMarkers();
	for (var i = 0; i < turns[index].length; i++) {
	    var turnOptions = 
		createTurnOptions("../markers/" + turns[index][i].icon);
	    var point = new GLatLng(turns[index][i].lat, turns[index][i].lon);
	    mgr.addMarker(createMarker(map, point, turnOptions, 100 + i, 
				       turns[index][i].html),
			  turns[index][i].min_zoom);
	}
	hasTurnIcons = true;
    }
}

function toggleTurnIcons(index) {
    if( hasTurnIcons ) {
	mgr.clearMarkers();
	hasTurnIcons = false;
    } else {
	addTurnIcons(index);
    }
}

function addSegments(index) {
    for( var i = 0; i < segments[index].length; i++ ) {
        map.addOverlay(createSegmentPolyline(map, 
					     segments[index][i].polyline, 
					     segments[index][i].roadHtml, 
					     segments[index][i].turnHtml,
					     segments[index][i].profileHtml));
    }
}

function clearOverlays(){
    map.clearOverlays();
    mgr.clearMarkers();
    parkingMarker = null;
    stopMarkers = null;
    poiMarkers = null;
    hasTurnIcons = false;
}

//****************************************************************
// PARKING DIRECTIONS
//****************************************************************

var parkingDirections;
var hasDirections = false;

function initParkingDirections() {
    hasDirections = false;
    parkingDirections = new GDirections(map, $("#park-directions").get(0));
    GEvent.addListener(parkingDirections, "addoverlay", function() {
	    centerAndZoomMap();
	    hasDirections = true;
	});
}

function loadParkingDirections(index) {
    var dirText = "from: " + $("#park-from").get(0).value + 
	" to: " + parking[index].lat + ", " + parking[index].lon;
    parkingDirections.load(dirText, {preserveViewport: true});
}

function clearParkingDirections() {
    parkingDirections.clear();
    hasDirections = false;
}

function addParkingDirectionsBounds(bounds) {
    var parkBounds = parkingDirections.getBounds();
    if( parkBounds != null) {
	bounds.extend(parkBounds.getSouthWest());
	bounds.extend(parkBounds.getNorthEast());
    }
}

function printableParkingDirections(index) {
    var dirUrl = "http://maps.google.com/maps?" + 
	"saddr=" + $("#park-from").get(0).value.replace(/[ \n]/g, "+") +
	"&daddr=" + parking[index].lat + "," + parking[index].lon;
    window.open(dirUrl);
}

//****************************************************************
// DISPLAY
//****************************************************************

function centerAndZoomMap() {
    var sw = new GLatLng(ride_bounds[rideIndex].min_lat, 
			 ride_bounds[rideIndex].min_lon);
    var ne = new GLatLng(ride_bounds[rideIndex].max_lat, 
			 ride_bounds[rideIndex].max_lon);
    var bounds = new GLatLngBounds(sw, ne);
    addParkingDirectionsBounds(bounds);
    map.setCenter(bounds.getCenter(), 
		  map.getBoundsZoomLevel(bounds));
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
    clearParkingDirections();
    clearOverlays();
    centerAndZoomMap();

    addParkingIcon(index);
    addStopIcons(index);
    addPOIIcons(index);
    addTurnIcons(index);
    addSegments(index);

    displayParking(index);
    displayInstructions(index);
    displayProfiles(index);
    displayStops(index);
    displayPOIs(index);
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
    if(showTabs) {
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
    map = new GMap2(document.getElementById("map-canvas"));
    if( ride_data.ride_type == "mtb" ) {
	map.setMapType(G_PHYSICAL_MAP);
    }
    map.setUIToDefault();
    initParkingDirections();
    centerAndZoomMap(); // redundant, but have to before calling ops on map
    mgr = new MarkerManager(map);

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
	if (GBrowserIsCompatible()) {
	    $("#no_js_warning").css("display", "none");
	    $("html,body").css("overflow", "hidden");
	    $("#header,#tabs,#map,#sab-copyright").css("display", "block");
	    $("#header,#tabs,#map,#sab-copyright").css("position", "absolute");
	    $("#tabs").tabs();
	    $(".prof-dialogs").dialog({ autoOpen: false, 
			height: 450, 
			width: 800 });
	    $(".help-dialogs").dialog({ autoOpen: false, 
			height: 450, 
			width: 800 });
	    layoutEverything();
	    initializeMap();
	    displayRide(rideIndex);

	    $(document.body).unload(function() {
		    GUnload();
		});

	    $(window).resize(function() {
		    layoutEverything();
		    map.checkResize();
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
			clearParkingDirections();
			displayRide(rideIndex);
			$('#over-ride-' + rideIndex).get(0).checked = true;
		    });
		var label = '#over-ride-' + i;
		$(label).data("index", i).click(function(event) {
			rideIndex = $(event.target).data("index");
			clearParkingDirections();
			displayRide(rideIndex);
			$('#header-ride-' + rideIndex).get(0).checked = true;
		    });
	    }

	    $(".parking-spans").click(function(event) {
		    var parts = event.target.id.split('-');
		    var ride = parseInt(parts[1], 10);
		    var point = 
			new GLatLng(parking[ride].lat, 
				    parking[ride].lon);
		    map.openInfoWindowHtml(point, parking[ride].html, infoOptions);
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
			new GLatLng(stops[ride][index].lat, 
				    stops[ride][index].lon);
		    map.openInfoWindowHtml(point, stops[ride][index].html, infoOptions);
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
			new GLatLng(pois[ride][index].lat, 
				    pois[ride][index].lon);
		    map.openInfoWindowHtml(point, pois[ride][index].html, infoOptions);
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
			    new GLatLng(segments[ride][index].mid_lat, 
					segments[ride][index].mid_lon);
			var roadTab = new GInfoWindowTab("Road", 
						     segments[ride][index].roadHtml);
			var profTab = new GInfoWindowTab("Profile", 
						     segments[ride][index].profileHtml);
			map.openInfoWindowTabsHtml(point, 
						   [roadTab, profTab], infoOptions);
		    }
		    else {
			point = 
			    new GLatLng(turns[ride][index].lat, 
					turns[ride][index].lon);
			map.openInfoWindowHtml(point, turns[ride][index].html, infoOptions);
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
			    new GLatLng(segments[ride][index].mid_lat, 
					segments[ride][index].mid_lon);
			roadTab = new GInfoWindowTab("Road", 
						     segments[ride][index].roadHtml);
			profTab = new GInfoWindowTab("Profile", 
						     segments[ride][index].profileHtml);
			map.openInfoWindowTabsHtml(point, 
						   [roadTab, profTab], infoOptions);
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
	    $(".show-park").click(function(event) {
		    toggleParkingIcon(rideIndex);
		});
	    $("#show-park-img").click(function(event) {
		    ckbox = $("#show-park-ck").get(0);
		    ckbox.checked = !ckbox.checked;
		    toggleParkingIcon(rideIndex);
		});
	    $(".show-stops").click(function(event) {
		    toggleStopIcons(rideIndex);
		});
	    $("#show-stops-img").click(function(event) {
		    ckbox = $("#show-stops-ck").get(0);
		    ckbox.checked = !ckbox.checked;
		    toggleStopIcons(rideIndex);
		});
	    $(".show-pois").click(function(event) {
		    togglePOIIcons(rideIndex);
		});
	    $("#show-pois-img").click(function(event) {
		    ckbox = $("#show-pois-ck").get(0);
		    ckbox.checked = !ckbox.checked;
		    togglePOIIcons(rideIndex);
		});
	    $(".show-turns").click(function(event) {
		    toggleTurnIcons(rideIndex);
		});
	    $("#show-turns-img").click(function(event) {
		    ckbox = $("#show-turns-ck").get(0);
		    ckbox.checked = !ckbox.checked;
		    toggleTurnIcons(rideIndex);
		});
	    $("#show-tabs-show").click(function(event) {
		    showTabs = true;

		    layoutEverything();
		    map.checkResize();
		    $("#tabs").show();
		    centerAndZoomMap();

		    $("#show-tabs-show").hide();
		    $("#show-tabs-hide").show();

		    event.preventDefault();
		});
	    $("#show-tabs-hide").click(function(event) {
		    showTabs = false;

		    $("#tabs").hide();
		    layoutEverything();
		    map.checkResize();
		    centerAndZoomMap();

		    $("#show-tabs-show").show();
		    $("#show-tabs-hide").hide();

		    event.preventDefault();
		});
	    $("#map-rezoom").click(function(event) {
		    centerAndZoomMap();
		    event.preventDefault();
		});

	    //********************
	    // parking directions
	    //********************
	    $("#park-submit").click(function(event) {
		    loadParkingDirections(rideIndex);
		    event.preventDefault();
		});
	    $("#park-clear").click(function(event) {
		    clearParkingDirections();
		    centerAndZoomMap();
		    event.preventDefault();
		});
	    $("#park-print").click(function(event) {
		    printableParkingDirections(rideIndex);
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
	}
    });
