#!/usr/bin/node

const argv = process.argv;
if (isNaN(argv[2])) {
  console.log('Missing size');
} else if (parseInt(argv[2]) > 0) {
  let i = 0;
  while (i < parseInt(argv[2])) {
    let j = 0;
    while (j < parseInt(argv[2])) {
      process.stdout.write('X');
      j++;
    }
    process.stdout.write('\n');
    i++;
  }
}
