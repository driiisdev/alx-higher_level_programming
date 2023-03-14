#!/usr/bin/node

const args = process.argv.slice(2).map((x) => {
  return parseInt(x);
});

if (args.length <= 1) {
  console.log(0);
} else {
  const maxsecond = args.sort(function (a, b) { return b - a; })[1];
  console.log(maxsecond);
}
