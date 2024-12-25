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
  let count = 0; // Counter to track how many character requests have been completed

  characters.forEach((character, index) => {
    request(character, (error, response, body) => {
      if (error) {
        console.error(`Error fetching character data: ${error}`);
      } else if (response.statusCode === 200) {
        const characterData = JSON.parse(body);
        // Here we add the character name to an array at the index it corresponds to in the characters array
        const names = [];
        names[index] = characterData.name;
        
        // Increment the count each time a character is successfully fetched
        count++;
        
        // Check if all characters have been processed
        if (count === characters.length) {
          // Log all names in the correct order
          names.forEach(name => {
            if (name) console.log(name); // Only log if the name was set
          });
        }
      }
    });
  });
});