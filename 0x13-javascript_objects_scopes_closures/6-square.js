#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    const sqrSize = this.width;
    if (c === undefined) {
      c = 'X';
    }
    for (let x = 0; x < sqrSize; x++) {
      console.log(c.repeat(sqrSize));
    }
  }
}

module.exports = Square;
