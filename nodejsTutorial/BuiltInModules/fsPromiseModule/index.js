const fs = require('node:fs/promises');

async function readFile() {
    console.log('Reading file...');

    try {
        const data = await fs.readFile('BuiltInModules/fsModule/file.txt', 'utf-8');
        console.log(data);
    }
    catch (err) {
        console.log(err)
    }
}

readFile();
console.log('Finished reading file...');
