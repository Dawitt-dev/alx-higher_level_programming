#!/usr/bin/node
const request = require('request');

// Get movie id
const movieId = process.argv[2];

// check if movie id is provided
if (!movieId) {
  console.error('please provide movie id');
  process.exit(1);
}

// Get API URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a Get request to the API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const film = JSON.parse(body);

  // print the title of the movie
  console.log(film.title);
});
