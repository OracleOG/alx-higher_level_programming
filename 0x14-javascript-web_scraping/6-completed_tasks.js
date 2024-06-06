#!/usr/bin/node
const request = require('request');

let completed = {};
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body)
  for (const task of data) {
    if (!(task.userId in completed)) {
        completed[task.userId] = 0
    }
    if (task.completed === true) {
        completed[task.userId] += 1
    }
  }
  console.log(completed)
});
