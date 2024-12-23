#!/usr/bin/node

const size = Number.parseInt(process.argv[2]);

if (!isNaN(size) && size > 0) {
  let line;
  for (let x = 0; size > x; x++) {
    line = '';
    for (let y = 0; size > y; y++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
