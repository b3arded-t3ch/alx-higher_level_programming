#!/usr/bin/node
const SquareN = require('./5-square');

class Square extends SquareN {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          s += 'X';
        } else {
          s += c;
        }
      }
      console.log(s);
    }
  }
}
module.exports = Square;
