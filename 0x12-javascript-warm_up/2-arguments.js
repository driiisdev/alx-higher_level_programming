#!/usr/bin/node

const nargv = process.argv.length - 2;

if (nargv === 0) {
  console.log('No argument');
} else if (nargv === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
