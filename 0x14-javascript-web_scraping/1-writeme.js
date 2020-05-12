#!/usr/bin/node
/* Write a script that writes a string to a file. */
/* read and write a file using fs module */
const fs = require('fs');

/* writes a string to a file from 1 arg to 2 arg Using utf-8 */
fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err, data) => {
  if (err) {
    /* If an error occurred during while writing, print the error object */
    return console.log(err);
  }
});
