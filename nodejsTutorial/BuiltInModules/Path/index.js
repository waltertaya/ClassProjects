const path = require('node:path')
// const path = require('path')
console.log(__filename);
console.log(__dirname);

// basename method in the path module which returns last portion of a path
console.log(path.basename(__filename));
console.log(path.basename(__dirname));

// extname method which returns the extension of the file
console.log(path.extname(__filename));
console.log(path.extname(__dirname));

// parse method which returns an object of the path
console.log(path.parse(__filename));

// path.format which returns a path string from an object
console.log(path.format(path.parse(__filename)));

// isAbsolute method which returns true if the path is absolute
console.log(path.isAbsolute(__filename));

// join method which joins the path segments into one path
console.log(path.join(__dirname, 'index.js'));

// resolve method which resolves the path segments into one path
console.log(path.resolve(__dirname, 'index.js'));