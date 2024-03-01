const fs = require('node:fs/promises');

console.log('Reading file...');

fs.readFile('BuiltInModules/fsModule/file.txt', 'utf-8')
    .then((data) => {
        console.log(data);
    })
    .catch((err) => {
        console.error(err);
    });

console.log('Finished reading file...');