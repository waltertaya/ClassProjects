const express = require('express');

const app = express();
const PORT = 8000;

// Register middleware
app.use(express.json());
app.use(express.urlencoded());

let laptops = [
    {
        name: 'Asus',
        number: 39
    }
]


app.listen(PORT, () => {
    console.log('Server is running on port: ' + PORT);
});

// Middleware using next function to call the next function
// app.get('/', (request, response, next) => {
//     console.log('Before handling request!')
//     next();
// }, (request, response) => {
//     response.send(laptops);
// });

app.get('/laptop', (request, response) => {
    response.send(laptops);
});

app.get('/laptop/:id', (request, response) => {
    const id = request.params.id;
    response.send(laptops[id]);
});

app.post('/laptop', (request, response) => {
    console.log(request.body);
    laptops.push(request.body);
    response.send(201);
});