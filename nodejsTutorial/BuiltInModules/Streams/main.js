const fs = require('node:fs');

const readableStream = fs.createReadStream('BuiltInModules/fsModule/file.txt', {encoding: 'utf8', highWaterMark: 4});

const writableStream = fs.createWriteStream('BuiltInModules/Streams/fileCopy.txt');

readableStream.on('data', (chunk) => {
    console.log(chunk);
  writableStream.write(chunk);
}
);