function initMap() {
  var location = { lat: 50.441679, lng: 2.805585 };
  var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 20,
    center: location,
  });
  var marker = new google.maps.Marker({
    position: location,
    map: map,
  });
}
