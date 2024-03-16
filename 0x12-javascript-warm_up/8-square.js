#!/usr/bin/node
const sqSize = process.argv[2];
const brick = 'X';
if (!parseInt(sqSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(sqSize); i++) {
    console.log(brick.repeat(sqSize));
  }
}
