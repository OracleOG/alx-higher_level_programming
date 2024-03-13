#!/usr/bin/node

function secondBigNum (numArray) {
  if (numArray.length < 2) {
    return 0;
  } else {
    let highest = 0;
    for (const element of numArray) {
      if (element > highest) {
        highest = element;
      }
    }
    let second = 0;
    for (const elements of numArray) {
      if (elements > second) {
        if (elements < highest) {
          second = elements;
        }
      }
    }
    return second;
  }
}

const argArray = process.argv.slice(2).map(Number);

console.log(secondBigNum(argArray));
