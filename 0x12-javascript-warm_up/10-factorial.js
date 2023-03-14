#!/usr/bin/node

const argv = process.argv;

function factorial (n) {
  if (n === 1 || isNaN(n)) {
    return 1;
  }
  return (n * factrl(n - 1));
}

const n = parseInt(argv[2]);
console.log(factorial(n));
