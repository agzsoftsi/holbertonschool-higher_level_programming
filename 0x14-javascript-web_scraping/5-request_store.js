#!/usr/bin/node
/*  Task 5 - script that gets the contents of a webpage and stores it in a file. */
/* module request ands fs module */
const request = require('request');
const fs = require('fs');

/* The first argument is the URL to request */
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  /* The second argument the file path to store the body response */
  fs.writeFile(process.argv[3], body, 'utf8', function (err, data) {
    if (err) throw err;
  });
});
