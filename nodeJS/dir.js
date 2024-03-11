const fs = require('fs');
const path = require('path');

if (fs.existsSync(path.join(__dirname, 'test'))) {
    console.log('The directory exists');
} else {
    fs.mkdir(path.join(__dirname, 'test'), () => {
        console.log('The directory has been created');
    });
}

if (fs.existsSync(path.join(__dirname, 'test'))) {
    fs.rmdir(path.join(__dirname, 'test'), () => {
        console.log('The directory has been removed from the filesystem');
    });
} else {
    console.log('The file does not exist!!!!!!!!!!!!!');
}