const http = require('node:http');

const server = http.createServer((req, res) => {

    const laptop = {
        type: 'laptop',
        brand: 'Apple',
        model: 'MacBook Pro',
        year: 2020
    };

    res.writeHead(200, {'Content-Type': 'application/json'});
    res.end(JSON.stringify(laptop));
});

server.listen(3000, () => {
    console.log('Server is running on port 3000');
});
