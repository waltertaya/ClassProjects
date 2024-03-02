const http = require('node:http');
const fs = require('node:fs');

const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/html'});
    // const html = fs.readFileSync('BuiltInModules/HTMLRes/index.html', 'utf8');
    // res.end(html);
    fs.createReadStream('BuiltInModules/HTMLRes/index.html').pipe(res);
});

server.listen(3000, () => {
    console.log('Server is running on port 3000');
});
