#!/usr/bin/node
const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const data1 = fs.readFileSync(file1, 'utf-8');
const data2 = fs.readFileSync(file2, 'utf-8');

fs.writeFileSync(process.argv[4], data1 + data2);
