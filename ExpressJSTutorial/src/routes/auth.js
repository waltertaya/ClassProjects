const Router = require('express');

const router = Router();

// router.post('/login', (request, response) => {
//     const { username, password } = request.body;
//     if (username === 'admin' && password === 'admin') {
//         request.session.user = username;
//         response.send('You are logged in!');
//     } else {
//         response.send('Username or password is incorrect');
//     }
// });

router.post('/login', (request, response) => {
    const { username, password } = request.body;
    if (username && password) {
        if (request.session.user) {
            response.send(request.session.user);
        } else {
            request.session.user = username;
            response.send(request.session);
        }
    } else {
        response.send(401);
    }
});

module.exports = router;