const fsPromises = require('fs').promises;
const path = require('path');

const fileOps = async () => {
    try {
        console.log('File operations started...');
        const data = await fsPromises.readFile(path.join(__dirname, 'files', 'test1.txt'), 'utf-8');
        await fsPromises.writeFile(path.join(__dirname, 'files', 'test3.txt'), data);
        await fsPromises.unlink(path.join(__dirname, 'files', 'test.txt'));
        await fsPromises.appendFile(path.join(__dirname, 'files', 'test1.txt'), '\n\n\New content added to the existing file');
        console.log('File operation completed');
    } catch (err) {
        console.error(err);
        return;
    }
};

fileOps();