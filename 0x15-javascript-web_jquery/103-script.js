$(document).ready(function() {
  function fetchTranslation() {
    const langCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

    $.get(apiUrl, function(data) {
      $('#hello').text(data.hello);
    }).fail(function() {
      $('#hello').text('Error fetching translation');
    });
  }

  // Fetch translation when the button is clicked
  $('#btn_translate').on('click', fetchTranslation);

  // Fetch translation when Enter key is pressed
  $('#language_code').on('keypress', function(event) {
    if (event.which == 13) {
      fetchTranslation();
    }
  });
});
