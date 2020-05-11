#!/usr/bin/node
/* Task Advanced 100 - Write a script that imports an array and computes a new array */
/* Your script must import list from the file 100-data.js */
const list = require('./100-data').list;
console.log(list);
/* A new list must be created with each value equal to the value of the initial list, multipled by the index in the list */
const map = list.map((x, i) => x * i);
console.log(map);
