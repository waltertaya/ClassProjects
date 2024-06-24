const express = require('express');
const multer = require('multer');
const bodyParser = require('body-parser');
const cors = require('cors'); // Add this line
const { Sequelize, DataTypes } = require('sequelize');

const app = express();
const port = 3000;

// Use CORS middleware
app.use(cors()); // Add this line

// Middleware to parse JSON bodies
app.use(bodyParser.json({ limit: '10mb' }));

// Configure Multer to store files in memory
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

// Setup Sequelize with MySQL
const sequelize = new Sequelize('ImageStore', 'root', 'Walter_8236!', {
    host: 'localhost',
    dialect: 'mysql'
});

// Define User model
const User = sequelize.define('User', {
    userId: {
        type: DataTypes.STRING,
        primaryKey: true
    },
    profileImage: {
        type: DataTypes.TEXT
    }
});

// Sync database
sequelize.sync();

// Route to upload image and save it as Base64 string
app.post('/upload', upload.single('image'), async (req, res) => {
    const userId = req.body.userId;
    const imageBuffer = req.file.buffer;
    const imageBase64 = imageBuffer.toString('base64');

    try {
        let user = await User.findOne({ where: { userId: userId } });
        if (user) {
            user.profileImage = imageBase64;
            await user.save();
        } else {
            user = await User.create({ userId: userId, profileImage: imageBase64 });
        }

        res.json({ message: 'Image uploaded successfully!' });
    } catch (error) {
        res.status(500).json({ message: 'Error uploading image', error: error.message });
    }
});

// Route to get image as Base64 string
app.get('/profile-image/:userId', async (req, res) => {
    const userId = req.params.userId;

    try {
        const user = await User.findOne({ where: { userId: userId } });

        if (user) {
            res.json({ imageBase64: user.profileImage });
        } else {
            res.status(404).json({ message: 'User not found' });
        }
    } catch (error) {
        res.status(500).json({ message: 'Error fetching image', error: error.message });
    }
});

// Route to get all images as Base64 strings
app.get('/profile-images', async (req, res) => {
    try {
        const users = await User.findAll();

        if (users.length > 0) {
            const images = users.map(user => ({ userId: user.userId, imageBase64: user.profileImage }));
            res.json(images);
        } else {
            res.status(404).json({ message: 'No users found' });
        }
    } catch (error) {
        res.status(500).json({ message: 'Error fetching images', error: error.message });
    }
});


app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
