#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error fetching film data: ${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  
  fetchCharacter = (url) => {
    return ( new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else if (response.statusCode === 200) {
          resolve(JSON.parse(body).name);
        }
      });
  }))
  };

  Promise.all(characters.map(fetchCharacter))
    .then((names) => {
      names.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.error(`Error fetching character data: ${error}`);
    });
});
