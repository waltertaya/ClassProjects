const fs = require('fs');
const path = require('path')

fs.readFile(path.join(__dirname, 'files', 'test1.txt'), 'utf-8', (err, data) => {
    if (err) throw err;
    // console.log(data.toString());
    console.log(data);
});

fs.writeFile(path.join(__dirname, 'files', 'test2.txt'), 'New contents added to the new file created', (err) => {
    if (err) throw err;
    console.log('File created and contents added');
});

fs.appendFile(path.join(__dirname, 'files', 'test2.txt'), '\n\nNew contents added to the existing file', (err) => {
    if (err) throw err;
    console.log('File created and contents added');
});