#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// charcter ID
const characterId = '18';

// check if API URL is provided
if (!apiUrl) {
  console.error('Please provide the API URL');
  process.exit(1);
}

// Make a GET request to the API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const films = JSON.parse(body).results;

  // Count the number of movies where "wedge Antilles"
  const count = films.filter(film =>
    film.characters.some(character => character.endsWith(`/${characterId}/`))
  ).length;

  // print the nuber of movies
  console.log(count);
});
