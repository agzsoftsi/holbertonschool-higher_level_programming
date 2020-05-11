#!/usr/bin/node
/* Write a class Square that defines a square and inherits from Square of 5-square.js */
const sq1 = require('./5-square');

class Square extends sq1 {
}

/* Create an instance method called charPrint(c) that prints the rectangle using the character c */
Square.prototype.charPrint = function (c) {
  /* If c is undefined, use the character X */
  if (!c) {
    c = 'X';
  }
  for (let i = 0; i < this.width; i++) {
    console.log(c.repeat(this.width));
  }
};

module.exports = Square;
