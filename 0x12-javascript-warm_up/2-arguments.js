#!/usr/bin/node

const numOfArg = process.argv.length - 2;

if (numOfArg === 0) {
  console.log('No argument');
} else if (numOfArg === 1) {
  console.log('Argument found');
} else if (numOfArg === 2) {
  console.log('Arguments found');
}
