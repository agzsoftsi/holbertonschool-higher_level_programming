#!/usr/bin/node
/* Write a function that prints the number of arguments already printed and the new argument value */
let n = 0;
exports.logMe = function (item) {
  /* <number arguments already printed>: <current argument value> */
  console.log(n + ': ' + item);
  n++;
};
