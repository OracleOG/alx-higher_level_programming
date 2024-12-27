$(document).ready(function() {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        data.results.forEach(film => {
            $('UL#list_movies').append('<li>' + film.title + '</li>');
        });
        
    });
    $.fail(function(xhr, textStatus, errorThrown) {
        console.error(textStatus, errorThrown);
    })
});
