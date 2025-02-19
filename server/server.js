const express = require('express'); // Importing express
const bodyParser = require('body-parser'); // Importing body-parser
const mongoose = require('mongoose'); // Importing mongoose
const cors = require('cors'); // Importing cors
const { createServer } = require('http'); // Importing http
const authRoutes = require('./routes/auth'); // Import the auth routes


// Configurations
require('dotenv').config();
const app = express();
const httpServer = createServer(app);


// Middlewares
app.use(cors({ origin: process.env.CLIENT_URL, credentials: true }));
app.use(bodyParser.json());
app.use(express.json());


// Routes
app.use('/api/auth', authRoutes); // Use the auth routes


// DB Connection
const MongoDB_URI = process.env.MONGO_URI || 'mongodb://localhost:27017/CN-Hackathon';
mongoose.connect(MongoDB_URI)
    .then(() => console.log('MongoDB Connected'))
    .catch(err => console.log(err));


// Server
const PORT = process.env.PORT || 5000;

httpServer.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});