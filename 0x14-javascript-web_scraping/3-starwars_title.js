#!/usr/bin/node
/* Task 3 - script that prints the title of a Star Wars movie where the episode number matches a given integer. */
/* use the module request */
const request = require('request');
/* use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id */
const url = 'http://swapi-api.hbtn.io/api/films/' + parseInt(process.argv[2]);
request(url, function (error, response, body) {
  if (error) throw error;
  /*  prints the title of a Star Wars movie where the episode number matches a given integer. */
  console.log(JSON.parse(body).title);
});
