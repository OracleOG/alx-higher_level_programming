#!/usr/bin/node

function add (a, b) {
  a = Number.parseInt(a);
  b = Number.parseInt(b);
  console.log(a + b);
  return a + b;
}

const firstArg = process.argv[2];
const secondArg = process.argv[3];

add(firstArg, secondArg);
