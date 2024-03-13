#!/usr/bin/node

const numArg = process.argv.length - 2;

if (numArg === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
