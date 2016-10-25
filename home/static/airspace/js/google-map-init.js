jQuery(document).ready(function() {
    "use strict";


    function b() {
        var a = {
                zoom: 16,
                scrollwheel: false,
                center: new google.maps.LatLng(29.9399014,-90.1218437),
                styles: [{
                    "featureType": "landscape",
                }]
            },
            b = document.getElementById("map"),
            c = new google.maps.Map(b, a);
        new google.maps.Marker({
            position: new google.maps.LatLng(29.9399014,-90.1218437),
            map: c,
            title: "Snazzy!"
        })
    }
    google.maps.event.addDomListener(window, "load", b);

});