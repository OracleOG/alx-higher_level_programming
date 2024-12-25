#!/usr/bin/node
const request = require('request');

const completed = {};
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  for (const task of data) {
    if (task.completed === true) {
      completed[task.userId] += 1;
    }
  }
  console.log(completed);
});
