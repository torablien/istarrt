jQuery(document).ready(function() {
    "use strict";

    function b() {
        var a = {
                zoom: 5,
                scrollwheel: false,
                center: new google.maps.LatLng(8.3848956,9.2657407),
                styles: [{
                    "featureType": "administrative",
                    "elementType": "labels.text.fill",
                    "stylers": [{
                        "color": "#c7c4c7"
                    }]
                }, {
                    "featureType": "administrative.country",
                    "elementType": "labels.text.stroke",
                    "stylers": [{
                        "color": "#6d438d"
                    }]
                }, {
                    "featureType": "administrative.province",
                    "elementType": "geometry.stroke",
                    "stylers": [{
                        "visibility": "off"
                    }]
                }, {
                    "featureType": "administrative.neighborhood",
                    "elementType": "geometry.fill",
                    "stylers": [{
                        "color": "#8e6ba8"
                    }]
                }, {
                    "featureType": "landscape",
                    "elementType": "geometry",
                    "stylers": [{
                        "lightness": "0"
                    }, {
                        "saturation": "0"
                    }, {
                        "color": "#f4f5f1"
                    }, {
                        "gamma": "1"
                    }]
                }, {
                    "featureType": "landscape.man_made",
                    "elementType": "all",
                    "stylers": [{
                        "lightness": "-3"
                    }, {
                        "gamma": "1.00"
                    }]
                }, {
                    "featureType": "landscape.natural.terrain",
                    "elementType": "all",
                    "stylers": [{
                        "visibility": "off"
                    }]
                }, {
                    "featureType": "poi",
                    "elementType": "all",
                    "stylers": [{
                        "visibility": "off"
                    }]
                }, {
                    "featureType": "poi",
                    "elementType": "geometry.fill",
                    "stylers": [{
                        "color": "#b59ac9"
                    }]
                }, {
                    "featureType": "poi.park",
                    "elementType": "geometry.fill",
                    "stylers": [{
                        "color": "#cbe2a7"
                    }, {
                        "visibility": "on"
                    }]
                }, {
                    "featureType": "road",
                    "elementType": "all",
                    "stylers": [{
                        "saturation": -100
                    }, {
                        "lightness": "65"
                    }, {
                        "visibility": "simplified"
                    }]
                }, {
                    "featureType": "road.highway",
                    "elementType": "all",
                    "stylers": [{
                        "visibility": "simplified"
                    }]
                }, {
                    "featureType": "road.highway",
                    "elementType": "geometry.fill",
                    "stylers": [{
                        "color": "#dbcce4"
                    }, {
                        "visibility": "simplified"
                    }]
                }, {
                    "featureType": "road.highway",
                    "elementType": "labels.text",
                    "stylers": [{
                        "color": "#4e4e4e"
                    }]
                }, {
                    "featureType": "road.arterial",
                    "elementType": "labels.text.fill",
                    "stylers": [{
                        "color": "#787878"
                    }]
                }, {
                    "featureType": "road.arterial",
                    "elementType": "labels.icon",
                    "stylers": [{
                        "visibility": "off"
                    }]
                }, {
                    "featureType": "transit",
                    "elementType": "all",
                    "stylers": [{
                        "visibility": "simplified"
                    }]
                }, {
                    "featureType": "transit",
                    "elementType": "geometry.fill",
                    "stylers": [{
                        "color": "#b59ac9"
                    }]
                }, {
                    "featureType": "transit",
                    "elementType": "labels.text.fill",
                    "stylers": [{
                        "color": "#947fa0"
                    }, {
                        "saturation": "-50"
                    }, {
                        "lightness": "0"
                    }]
                }, {
                    "featureType": "transit.line",
                    "elementType": "geometry.fill",
                    "stylers": [{
                        "color": "#b59ac9"
                    }]
                }, {
                    "featureType": "transit.line",
                    "elementType": "labels.text.fill",
                    "stylers": [{
                        "lightness": "0"
                    }]
                }, {
                    "featureType": "transit.station.airport",
                    "elementType": "labels.icon",
                    "stylers": [{
                        "hue": "#0a00ff"
                    }, {
                        "saturation": "-77"
                    }, {
                        "gamma": "0.57"
                    }, {
                        "lightness": "0"
                    }]
                }, {
                    "featureType": "transit.station.rail",
                    "elementType": "labels.text.fill",
                    "stylers": [{
                        "color": "#8f7f93"
                    }, {
                        "lightness": "0"
                    }]
                }, {
                    "featureType": "transit.station.rail",
                    "elementType": "labels.icon",
                    "stylers": [{
                        "lightness": "42"
                    }, {
                        "gamma": "0.75"
                    }, {
                        "saturation": "-68"
                    }, {
                        "hue": "#9200ff"
                    }]
                }, {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": [{
                        "color": "#eaf6f8"
                    }, {
                        "visibility": "on"
                    }]
                }, {
                    "featureType": "water",
                    "elementType": "geometry.fill",
                    "stylers": [{
                        "color": "#cee5f2"
                    }]
                }, {
                    "featureType": "water",
                    "elementType": "labels.text.fill",
                    "stylers": [{
                        "lightness": "-49"
                    }, {
                        "saturation": "-53"
                    }, {
                        "gamma": "0.79"
                    }]
                }]

            },

            b = document.getElementById("map"),

            c = new google.maps.Map(b, a);

        new google.maps.Marker(
            {
                position: new google.maps.LatLng(-1.2920659, 36.821946),
                map: c,
                title: "Nairobi, Kenya"
            })
            
            new google.maps.Marker({
                position: new google.maps.LatLng(5.5913754,-0.2497703),
                map: c,
                title: "Accra, Ghana"
            })
           new google.maps.Marker({
                position: new google.maps.LatLng(13.4680941,-16.6977596),
                map: c,
                title: "Farahja, Gambia"
            })
            new google.maps.Marker({
                position: new google.maps.LatLng(8.9423089,7.0605375),
                map: c,
                title: "Gwagwalada, Nigeria"
            })
            new google.maps.Marker({
                position: new google.maps.LatLng(2.7754066,32.2529404),
                map: c,
                title: "Gulu, Uganda"
            })
            new google.maps.Marker({
                position: new google.maps.LatLng(30.0218667,-90.0225578),
                map: c,
                title: "New Orleans"
            })
        
    }

    google.maps.event.addDomListener(window, "load", b);
});
