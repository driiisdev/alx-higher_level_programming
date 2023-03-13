#!/usr/bin/node

const argv = process.argv;

if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  const n = parseInt(argv[2]);
  console.log(`My number: ${n}`);
}
