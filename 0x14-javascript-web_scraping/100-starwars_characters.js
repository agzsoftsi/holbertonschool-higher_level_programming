#!/usr/bin/node
/* Task 100 - script that prints all characters of a Star Wars movie */
const request = require('request');
/* The first argument is the Movie ID - example: 3 = "Return of the Jedi */
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) throw error;
  for (const character of JSON.parse(body).characters) {
    request(character, function (error, response, body) {
      if (error) throw error;
      /* Display one character name by line */
      console.log(JSON.parse(body).name);
    });
  }
});
