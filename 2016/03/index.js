/* eslint-env: node */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const filePath = path.join(__dirname, 'input.txt');
const rl = readline.createInterface({
  input: fs.createReadStream(filePath),
  output: process.stdout,
  terminal: false,
});


function isValidTriangle(a, b, c, debug = false) {
  const result = (a + b > c) && (a + c > b) && (b + c > a);
  if (debug) {
    console.log(`${a} ${b} ${c}: ${result}`);
  }
  return result;
}

let count = 0;
let validCount = 0;

const input = [];

rl.on('line', (line) => {
  const a = parseInt(line.substring(2, 5).trim(), 10);
  const b = parseInt(line.substring(7, 10).trim(), 10);
  const c = parseInt(line.substring(12).trim(), 10);

  input.push([a, b, c]);
});

rl.on('close', () => {
  const rows = input.length;
  for (let y = 0; y < rows; y += 3) {
    for (let x = 0; x < 3; x += 1) {
      count += 1;
      if (isValidTriangle(input[y][x], input[y + 1][x], input[y + 2][x])) {
        validCount += 1;
      }
    }
  }
  console.log(`Total: ${count} Valid: ${validCount}`);
});

