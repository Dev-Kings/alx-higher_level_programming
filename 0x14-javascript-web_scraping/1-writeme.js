#!/usr/bin/node
// writing a string to a file
const fs = require('fs');
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
