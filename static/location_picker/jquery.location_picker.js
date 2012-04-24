$(document).unload(function(){
    google.maps.Unload();
});

$(document).ready(function(){
    $("input.location_picker").each(function (i) {
        var me = $(this),
            mapDiv = $('<div>').insertBefore(me).addClass('location_picker_map');

        me.css('display','none');

        var lat = -43.531065;
        var lng = 172.636671;
        if (me.val().split(/,\s*/).length == 2) {
            values = this.value.split(',');
            lat = values[0];
            lng = values[1];
        }
        var center = new google.maps.LatLng(lat, lng);

        var map = new google.maps.Map(mapDiv[0], {
            zoom: 15,
            center: center,
            scaleControl: true,
            navigationControl: true,
            navigationControlOptions: {
                position: google.maps.ControlPosition.RIGHT
            },
            disableDefaultUI: true,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });

        var marker = new google.maps.Marker({
            position: center,
            map: map
        });

        google.maps.event.addListener(map, 'click', function (e) {
            me.val(e.latLng.lat() + ',' + e.latLng.lng());
            marker.setPosition(e.latLng);
        });
    });
});
