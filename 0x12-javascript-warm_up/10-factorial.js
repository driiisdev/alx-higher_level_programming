#!/usr/bin/node

const argv = process.argv;

function factrl (n) {
  if (n === 0) {
    return 1;
  }
  return (n * factrl(n - 1));
}

if (!isNaN(argv[2])) {
  console.log(factrl(parseInt(argv[2])));
} else { console.log('NaN'); }
