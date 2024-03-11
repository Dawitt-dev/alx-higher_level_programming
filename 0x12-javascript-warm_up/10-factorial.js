#!/usr/bin/node

function factorial (n) {
  // Base case: factorial of 0 or 1 is 1
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    // Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1);
  }
}

if (process.argv.length !== 3) {
  console.log('1');
} else {
  const inputNumber = parseInt(process.argv[2]);
  const result = factorial(inputNumber);
  console.log(result);
}
