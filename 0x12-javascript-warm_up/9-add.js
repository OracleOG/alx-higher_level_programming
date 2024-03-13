#!/usr/bin/node

function add (a, b) {
  const val = process.argv;
  a = Number(val[2]);
  b = Number(val[3]);
  console.log(a + b);
}

add();
