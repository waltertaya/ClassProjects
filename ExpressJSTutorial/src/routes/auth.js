const Router = require('express');
const User = require('../database/schemas/User');

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

router.post('/register', async (req, res) => {
    const { username, password, email } = req.body;
    const userDB = await User.findOne({ $or: [{ username }, { email }]})
    if (userDB) {
        res.status(400).send({ msg: 'User already exists!' })
    } else {
        const newUser = await User.create({ username, password, email });
        // newUser.save();
        res.send(201)
    }
});

module.exports = router;