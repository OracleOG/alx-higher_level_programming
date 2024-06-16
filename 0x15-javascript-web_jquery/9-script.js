$(document).ready(function() {
    var url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    $.getJSON(url, function(data) {
        var namee = data.hello;
        $('DIV#hello').text(namee); 
    })
    });