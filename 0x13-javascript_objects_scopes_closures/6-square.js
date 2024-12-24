#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    for (let x = 0; x < this.height; x++) {
      let str = '';
      for (let y = 0; y < this.width; y++) {
        if (c !== undefined) {
          str += c;
        } else {
          str += 'X';
        }
      }
      console.log(str);
    }
  }
}

module.exports = Square;
