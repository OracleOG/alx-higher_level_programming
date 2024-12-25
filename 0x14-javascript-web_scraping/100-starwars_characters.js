#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response && response.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;
    characters.forEach(character => {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
          return;
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  }
});
