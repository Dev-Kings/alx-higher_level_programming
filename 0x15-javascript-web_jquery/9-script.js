$(document).ready(function() {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    $('#hello').html(data['hello']);
  });
});
