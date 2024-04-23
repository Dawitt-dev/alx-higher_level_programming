#!/usr/bin/node
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Check if file path is provided
if (!filePath) {
  console.error('please provide the file path as argument');
  process.exit(1);
}

// Read the content of the file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
