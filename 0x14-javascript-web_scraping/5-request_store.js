#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Check if URL and file path are provided
if (!url || !filePath) {
  console.error('Please provide the URL and file path as arguments.');
  process.exit(1);
}

// Make a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Write the body response to the file
  fs.writeFile(filePath, body, 'utf8', err => {
    if (err) {
      console.error('Error writing to file:', err);
    }
  });
});
