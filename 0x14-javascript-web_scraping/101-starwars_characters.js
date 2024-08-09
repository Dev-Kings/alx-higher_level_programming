#!/usr/bin/node

import request from 'request';

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films';
const fullURL = `${url}/${movieId}`;

request(fullURL, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  // Function to fetch and print each character in order
  function printCharacter (index) {
    if (index >= characters.length) return;

    request(characters[index], (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);

      // Recursively call printCharacter for the next character
      printCharacter(index + 1);
    });
  }

  printCharacter(0);
});
