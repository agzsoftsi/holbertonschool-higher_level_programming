#!/usr/bin/node
/* Task 5 - Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js */
const Rectangle = require('./4-rectangle');

/* You must use the class notation for defining your class and extends */
class Square extends Rectangle {
  constructor (size) {
    /* The constructor of Rectangle must be called (by using super()) */
    super(size, size);
  }
}

module.exports = Square;
