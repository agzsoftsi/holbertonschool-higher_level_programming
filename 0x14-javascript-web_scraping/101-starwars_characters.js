#!/usr/bin/node
/* script that prints all characters of a Star Wars movie */
const request = require('request');
/* first argument is the Movie ID - example: 3 = "Return of the Jedi" */
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

const start = function () {
  request(url, function (error, response, body) {
    if (error) throw error;
    end(JSON.parse(body).characters, 0);
  });
};

const end = function (characters, i) {
  if (characters.length === i) {
    return;
  }
  /* Display one character name by line in the same order of the list "characters" in the /films/ response */
  request(characters[i], function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    end(characters, ++i);
  });
};

start();
