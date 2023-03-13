#!/usr/bin/node

const argv = process.argv;
if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else if (parseInt(argv[2]) > 0) {
  let i = 0;
  while (i < parseInt(argv[2])) {
    console.log('C is fun');
    i++;
  }
}
