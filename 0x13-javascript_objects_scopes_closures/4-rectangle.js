#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let str = '';
      for (let y = 0; y < this.width; y++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    const newHeight = this.height;
    this.height = this.width;
    this.width = newHeight;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
