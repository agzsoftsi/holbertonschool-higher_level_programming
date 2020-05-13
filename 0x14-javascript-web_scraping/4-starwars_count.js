#!/usr/bin/node
/* script that prints the number of movies where the character "Wedge Antilles" is present. */
const request = require('request');
/* The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/ */
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) throw error;
  let con = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
	/* Wedge Antilles is character ID 18 */
        con++;
      }
    }
  }
  console.log(con);
});
