#!/usr/bin/node
const firstArg = Number.parseInt(process.argv[2]);
if (firstArg === undefined || isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; firstArg > x; x++) {
    console.log('C is fun');
  }
}
