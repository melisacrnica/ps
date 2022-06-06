/**
 * @param  {H.Map} map      A HERE Map instance within the application
 
*/
  
function addMarkersToMap(map) {
    var tuxpanMarker = new H.map.Marker({lat: 19.557268, lng: -103.378946});
    map.addObject(tuxpanMarker);

    var guadalajaraMarker = new H.map.Marker({lat: 20.6596988, lng: -103.34960920000003});
    map.addObject(guadalajaraMarker);

    var puertoVallarta = new H.map.Marker({lat: 20.653407, lng: -105.2253316});
    map.addObject(puertoVallarta);

    var losAngelesMarker = new H.map.Marker({lat: 34.0522342, lng: -118.2436849});
    map.addObject(losAngelesMarker);

    var cancunMarker = new H.map.Marker({lat: 21.161908, lng: -86.8515279});
    map.addObject(cancunMarker);
}

  
  //Step 1: initialize communication with the platform
  // In your own code, replace variable window.apikey with your own apikey
  var platform = new H.service.Platform({
    apikey: "ugMs-ffvphvzsWuyMsQ5ZDlo4ajFgllmavHTxfj5O6A"
  });
  var defaultLayers = platform.createDefaultLayers();
  
  //Step 2: initialize a map
  var map = new H.Map(document.getElementById('map'),
    defaultLayers.vector.normal.map, {
    center: {lat: 20.6596988, lng: -103.34960920000003},
    zoom: 8,
    pixelRatio: window.devicePixelRatio || 1
  });
  // add a resize listener to make sure that the map occupies the whole container
  window.addEventListener('resize', () => map.getViewPort().resize());
  
  //Step 3: make the map interactive
  // MapEvents enables the event system
  // Behavior implements default interactions for pan/zoom (also on mobile touch environments)
  var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
  
  // Create the default UI components
  var ui = H.ui.UI.createDefault(map, defaultLayers);
  

window.onload = function () {
    addMarkersToMap(map);
}