#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  try {
    const data = JSON.parse(body);

    console.log(data.title);
  } catch (e) {
    console.error('Error parsing JSON:', e);
  }
});
