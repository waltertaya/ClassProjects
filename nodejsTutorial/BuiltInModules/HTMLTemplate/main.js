const fs = require('node:fs');
const http = require('node:http');

const server = http.createServer((req, res) => {
    try {
        res.writeHead(200, { 'Content-Type': 'text/html' });

        const name = 'Walter Mitty';
        let html = fs.readFileSync('/home/waltermitty/ClassProjects/nodejsTutorial/BuiltInModules/HTMLTemplate/index.html', 'utf-8');
        html = html.replace('{{username}}', name);
        res.end(html);
    } catch (error) {
        console.log(error);
    }
});

server.listen(3000, () => {
    console.log('Server is listening on port 3000');
});
