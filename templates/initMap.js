function initMap() {
    const myLatlng = { lat: 26, lng: -24 };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 3,
      center: myLatlng,
    });
    // Create the initial InfoWindow.
    let infoWindow = new google.maps.InfoWindow({
      content: "Click the map to get Lat/Lng!",
      position: myLatlng,
    });
    infoWindow.open(map);
    // Configure the click listener.
    map.addListener("click", (mapsMouseEvent) => {
      // Close the current InfoWindow.
      infoWindow.close();

      // delete json stuff so it's just the coordinates
      var str = JSON.stringify(mapsMouseEvent.latLng.toJSON());
      var str2 = str.replace('{"lat":', '').toString();
      var str3 = str2.replace('"lng":', '').toString();
      var str4 = str3.replace('}', '');

      // Link to the api
      var link = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+ str4.toString() +'&key=AIzaSyCy4rMsW8E0G5S7kJAH6rgXOPOl6MizZsw&language=en&result_type=country';
      
      // Get info from Geocoding API
      $(document).ready(function() {
        $.getJSON(link, function(data) {
          // Display country name
          document.getElementById('test').innerHTML = data.results[0].formatted_address;
        });
      });


      // Create a new InfoWindow.
      infoWindow = new google.maps.InfoWindow({
        position: mapsMouseEvent.latLng,
      });
      infoWindow.setContent(
        link
        //'https://maps.googleapis.com/maps/api/geocode/json?latlng='+ str4.toString() +'&key=AIzaSyCy4rMsW8E0G5S7kJAH6rgXOPOl6MizZsw&language=en&result_type=country'
      );
      infoWindow.open(map);
    });
  }