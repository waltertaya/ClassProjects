const express = require('express');
const session = require('express-session');
const cookieParser = require('cookie-parser');
const authRoute = require('./routes/auth');
const laptopRoutes = require('./routes/laptops');
const laptopPartsRoutes = require('./routes/laptopComp');

require('./database')

const app = express();
const PORT = 8000;

const APP_SECRET = ""
// Register middleware
app.use(cookieParser());
app.use(session({
    secret: `${APP_SECRET}`,
    resave: false,
    saveUninitialized: false,
}));

app.use(express.json());
app.use(express.urlencoded());
app.use('/api/v1/laptop', laptopRoutes);
app.use('/api/v1/laptopComp', laptopPartsRoutes);
app.use('/api/v1/auth', authRoute);

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
