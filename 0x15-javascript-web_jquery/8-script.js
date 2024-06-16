$(document).ready(function() {
    var url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    $.getJSON(url, function(data) {
        var films = data.results
        for (const value of films) {
            var title = value['title'];
            $('UL#list_movies').append('<li>' + title + '</li>');
        }
    } )
    });
