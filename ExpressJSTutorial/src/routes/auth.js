const Router = require('express');
const User = require('../database/schemas/User');
const { hashPassword, comparePassword } = require('../utils/helpers');

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

router.post('/login', async (request, response) => {
    const { email, password } = request.body;
    if (!email || !password) return response.send(400);
    const userDB = await User.findOne({ email });
    if (!userDB) return response.send(401);
    const isValid = comparePassword(password, userDB.password);
    if (isValid) {
        request.session.user = userDB;
        return response.send(200);
    } else {
        return response.send(401);
    }
});

router.post('/register', async (req, res) => {
    const { email } = req.body;
    const userDB = await User.findOne({ email })
    if (userDB) {
        res.status(400).send({ msg: 'User already exists!' })
    } else {
        const password = hashPassword(req.body.password);
        console.log(password);
        const newUser = await User.create({ email, password });
        // newUser.save();
        res.send(201)
    }
});

module.exports = router;