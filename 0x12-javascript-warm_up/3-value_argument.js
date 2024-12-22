#!/usr/bin/node

const { argv } = require('process');

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  argv.forEach((val, index) => {
    if (index > 1) {
      console.log(val);
    }
  });
}
