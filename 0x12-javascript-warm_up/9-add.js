#!/usr/bin/node

const argv = process.argv;

if ((!isNaN(argv[2])) && (!isNaN(argv[3]))) {
  console.log(parseInt(argv[2]) + parseInt(argv[3]));
} else { console.log('NaN'); }
