const fs = require('node:fs');

console.log('First')
const fileContents = fs.readFileSync('BuiltInModules/fsModule/file.txt', 'utf-8');
console.log(fileContents);

console.log('Second')
fs.readFile('BuiltInModules/fsModule/file.txt', 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});

console.log('Third')

fs.writeFileSync('BuiltInModules/fsModule/file1.txt', 'Hello World', 'utf-8');

fs.writeFileSync('BuiltInModules/fsModule/file2.txt', 'Hello World', {flag: 'a'}, 'utf-8', (err) => {
    if (err) {
        console.log(err);
        return;
    }
    console.log('File written successfully');
});