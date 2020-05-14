/* Task 8 -script that fetches and lists all movies title by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
All movie titles must be list in the HTML tag UL#list_movies
You must use the jQuery API
Use getJSON to call the API for starwars
*/
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (query) {
  query.results.forEach(function (movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
