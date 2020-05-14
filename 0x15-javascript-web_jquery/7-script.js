/* Task 7 -script that fetches and replaces the name of this URL: https://swapi-api.hbtn.io/api/people/5/?format=jsonThe name must be displayed in the HTML tag DIV#character
You must use the jQuery API
Use getJSON to call the API for starwars
*/
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (query) {
  $('#character').text(query.name);
});
