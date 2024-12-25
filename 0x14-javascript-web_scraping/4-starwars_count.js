#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;

    for (const film of data.results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }

    console.log(count);
  }
});
