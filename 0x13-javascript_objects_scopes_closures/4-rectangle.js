#!/usr/bin/node
/* Task 4 - Write a class Rectangle that defines a rectangle */
class Rectangle {
  constructor (w, h) {
    /* If w or h is equal to 0 or not a positive integer, create an empty object */
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

/* Create an instance method called print() that prints the rectangle using the character X */
Rectangle.prototype.print = function () {
  for (let i = 0; i < this.height; i++) {
    console.log('X'.repeat(this.width));
  }
};

/* Create an instance method called rotate() that exchanges the width and the height of the rectangle */
Rectangle.prototype.rotate = function () {
  [this.width, this.height] = [this.height, this.width];
};

/* Create an instance method called double() that multiples the width and the height of the rectangle by 2 */
Rectangle.prototype.double = function () {
  this.width *= 2;
  this.height *= 2;
};

module.exports = Rectangle;
