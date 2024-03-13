#!/usr/bin/node

function fact (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}

const num = Number(process.argv[2]);

console.log(fact(num));
