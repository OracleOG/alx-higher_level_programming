#!/usr/bin/node

const strNumber = process.argv[2];
const newNumber = Number.parseInt(strNumber);

if (isNaN(newNumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + newNumber);
}
