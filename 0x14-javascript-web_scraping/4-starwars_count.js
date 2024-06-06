#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  try {
    const result = JSON.parse(body);
    const data = result.results;
    let filmcount = 0;

    for (const film of data) {
      for (const film18 of film.characters) {
        if (film18.search('18') > 0) {
          filmcount++;
        }
      }
    }

    console.log(filmcount);
  } catch (e) {
    console.error('Error parsing JSON:', e);
  }
});
