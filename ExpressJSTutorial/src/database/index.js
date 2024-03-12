const mongoose = require('mongoose');
mongoose
    .connect('mongodb+srv://<username>:<password>@waltertayadb.y2nbk2w.mongodb.net/')
    .then(() => console.log('Connected to DB'))
    .catch((error) => console.log(error));

module.exports = mongoose;