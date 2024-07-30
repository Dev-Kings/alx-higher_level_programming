#!/usr/bin/node
// printing all characters of a Star Wars movie
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, function (error, result, body) {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  characters.forEach(characterUrl => {
    request(characterUrl, function (characterErr, characterRes, characterBody) {
      if (characterErr) {
        console.error(characterErr);
        return;
      }
      console.log(JSON.parse(characterBody).name);
    });
  });
});
