const http = require('node:http');

const server = http.createServer((req, res) => {
    // req.method => GET, POST, DELETE, PUT
    if(req.url === '/') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end('<h1>Home Page</h1>');
    } else if(req.url === '/about') {
        res.writeHead(200, {'Content-Type': 'text/html'});7
        res.end('<h1>About Page</h1>');
    } else if (req.url === '/api') {
        res.writeHead(200, {'Content-Type': 'application/json'})
        const obj = {
            name: 'Walter Mitty',
            laptop: 'Asus',
            Field: 'Software Engineering and Machine Learning',
            username: '@waltertaya'
        };
        res.end(JSON.stringify(obj));
    } else {
        res.writeHead(404)
        res.end('Page not found')
    }
});

server.listen(8000, () => {
    console.log('Server running at port 8000')
});