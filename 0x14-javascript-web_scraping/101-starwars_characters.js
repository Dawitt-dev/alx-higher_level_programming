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

  // Function to fetch character details and print their names
  const fetchAndPrintCharacters = async () => {
    for (const characterUrl of movie.characters) {
      try {
        const characterResponse = await new Promise((resolve, reject) => {
          request.get(characterUrl, (error, response, body) => {
            if (error) reject(error);
            else resolve(JSON.parse(body).name);
          });
        });
        console.log(characterResponse);
      } catch (error) {
        console.error('Error:', error);
      }
    }
  };

  // Call the function to fetch and print character names
  fetchAndPrintCharacters();
});
