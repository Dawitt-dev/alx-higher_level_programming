#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Check if movie ID is provided
if (!movieId) {
  console.error('Please provide the movie ID as an argument.');
  process.exit(1);
}

// Define the Star Wars API endpoint URL for the specified movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the JSON response body
  const movie = JSON.parse(body);

  // Print the names of all characters in the movie
  movie.characters.forEach(characterUrl => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
