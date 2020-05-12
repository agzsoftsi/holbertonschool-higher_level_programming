#!/usr/bin/node
/* Write a script that concats 2 files */
/* The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination */
const fs = require('fs');
for (let i = 2; i <= 3; i++) {
  fs.readFile(process.argv[i], 'utf8', function (err, data) {
    if (err) throw err;
    fs.appendFile(process.argv[4], data, (err) => {
      if (err) throw err;
    });
  });
}
