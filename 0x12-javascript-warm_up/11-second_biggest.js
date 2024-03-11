#!/usr/bin/node

function secondBiggest (args) {
  const numbers = args.map(Number);

  if (numbers.length <= 2) {
    return 0;
  }

  const uniqueNumbers = [...new Set(numbers)];
  const sortedNumbers = uniqueNumbers.sort((a, b) => b - a);

  return sortedNumbers[1];
}

const result = secondBiggest(process.argv.slice(2));
console.log(result);
