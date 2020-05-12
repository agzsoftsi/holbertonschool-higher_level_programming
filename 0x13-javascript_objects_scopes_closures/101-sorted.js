#!/usr/bin/node
/* Task 101 - script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.  import dict from the file 101-data.js */
const dict = require('./101-data').dict;
const sort = (obj) => {
  const reverse = {};
  /* A key is a number of occurrences - A value is the list of user ids */
  Object.keys(obj).forEach((key) => {
    reverse[obj[key]] = reverse[obj[key]] || [];
    reverse[obj[key]].push(key);
  });
  return reverse;
};
console.log(sort(dict));
