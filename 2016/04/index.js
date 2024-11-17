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

const input = [];

class EncryptedName {
  static countLetters(name) {
    const map = {};
    for (let i = 0; i < name.length; i += 1) {
      const c = name[i];
      if (c !== '-') {
        let count = 1;
        if (c in map) {
          count = map[c] + 1;
        }
        map[c] = count;
      }
    }
    const result = [];
    for (const k in map) {
      if ({}.hasOwnProperty.call(map, k)) {
        result.push({ key: k, value: map[k] });
      }
    }
    return result;
  }

  constructor(line) {
    const len = line.length;
    this.checksum = line.substring(len - 6, len - 1);
    let pos = len - 8;
    while (pos > 0) {
      if (line[pos] === '-') {
        break;
      }
      pos -= 1;
    }
    this.sector = parseInt(line.substring(pos + 1, len - 7), 10);
    this.name = line.substring(0, pos);
    this.map = EncryptedName.countLetters(this.name);
  }

  calculateChecksum() {
    this.map.sort((a, b) => {
      if (a.value > b.value) {
        return -1;
      }
      if (a.value < b.value) {
        return 1;
      }
      // tiebreaker
      if (a.key < b.key) {
        return -1;
      }
      if (a.key > b.key) {
        return 1;
      }
      return 0;
    });

    const result = [];
    for (let i = 0; i < 5; i += 1) {
      result.push(this.map[i].key);
    }
    return result.join('');
  }

  unshiftName() {
    const result = [];
    const offset = this.sector % 26;
    for (let i = 0; i < this.name.length; i += 1) {
      if (this.name[i] === '-') {
        result.push(' ');
      } else {
        let code = this.name[i].charCodeAt();
        code += offset;
        if (code > 122) {
          code -= 26;
        }
        result.push(String.fromCharCode(code));
      }
    }
    return result.join('');
  }
}

rl.on('line', (line) => {
  input.push(line);
});

rl.on('close', () => {
  const rows = input.length;
  let total = 0;

  input.forEach((item) => {
    const en = new EncryptedName(item);
    const chk = en.calculateChecksum();
    // console.log(`${en.name} ${en.sector} ${en.checksum}  ${chk}`);
    if (en.checksum === chk) {
      const decrypted = en.unshiftName();
      // if (decrypted.includes('north pole')) {
      console.log(`${en.sector} = ${decrypted}`);
      // }
    }
  });
});

