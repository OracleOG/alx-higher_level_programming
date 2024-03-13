#!/usr/bin/node

const strNumber = process.argv[2];
const newNumber = Number(strNumber);

if (isNaN(newNumber)) {
  console.log('Not a number');
} else {
  console.log(Number(strNumber));
}
