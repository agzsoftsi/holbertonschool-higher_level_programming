#!/usr/bin/node
/* Task 2 - script that display the status code of a GET request. */
/* use the module request */
const request = require('request');
/* first argument is the URL to request (GET) */
request(process.argv[2], function (error, response) {
  if (error) throw error;
  /* status code must be printed like this: code: <status code> */
  console.log('code: ' + response.statusCode);
});
