$(document).ready(function() {
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
        
        $('DIV#character').text(data.name);
    });
    $.fail(function(xhr, textStatus, errorThrown) {
        console.error(textStatus, errorThrown);
    })
});
