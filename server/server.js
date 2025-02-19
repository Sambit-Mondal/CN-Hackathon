import express from 'express'; // Importing express
import bodyParser from 'body-parser'; // Importing body-parser
import mongoose from 'mongoose'; // Importing mongoose
import cors from 'cors'; // Importing cors
import dotenv from 'dotenv'; // Importing dotenv
import axios from 'axios'; // Importing axios
import { createServer } from 'http'; // Importing http

// Configurations
const app = express();
const httpServer = createServer(app);
dotenv.config();


// Middlewares
app.use(bodyParser.json({ limit: "30mb", extended: true }));
app.use(bodyParser.urlencoded({ limit: "30mb", extended: true }));
app.use(cors({ origin: process.env.CLIENT_URL, credentials: true }));


// Routes


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