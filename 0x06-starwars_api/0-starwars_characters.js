#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${filmId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(response.statusMessage);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  fetchCharacters(charactersUrls);
});

function fetchCharacters (urls) {
  urls.forEach(url => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(response.statusMessage);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
}
