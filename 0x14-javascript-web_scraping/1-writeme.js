#!/usr/bin/node
const fs = require('fs');

// Get file path
const filePath = process.argv[2];

// Get string content to be written
const stringContent = process.argv[3];

// check if file path provided
if (!filePath) {
  console.error('please provide file path as an argument');
  process.exit(1);
}

// write the content on file
fs.writeFile(filePath, stringContent, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
