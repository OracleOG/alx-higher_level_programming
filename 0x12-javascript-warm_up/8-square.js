#!/usr/bin/node
const myArgv = process.argv[2];

if (isNaN(myArgv)) {
  console.log('Missing size');
} else {
  for (let x = 0; myArgv > x; x++) {
    let line = '';
    for (let y = 0; myArgv > y; y++) {
      line += 'X';
    }
    console.log(line);
  }
}
