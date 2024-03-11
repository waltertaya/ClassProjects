const fs = require('fs');

const rs = fs.createReadStream('./files/test1.txt', {'encoding': 'utf-8'});
const ws = fs.createWriteStream('./files/test.txt');

// rs.on('data', (chunk) => {
//     ws.write(chunk);
// });

rs.pipe(ws);
