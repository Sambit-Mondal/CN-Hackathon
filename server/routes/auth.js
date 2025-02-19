const express = require('express');
const { signup, login } = require('../controllers/authController');
const { validateSignup, validateLogin } = require('../middlewares/validateInput');
const Store = require('../models/store');

const router = express.Router();

router.post('/signup', validateSignup, signup);
router.post('/login', validateLogin, login);

// Fetch user details by email
router.get('/user/:email', async (req, res) => {
    try {
        const store = await Store.findOne({ email: req.params.email });
        if (!store) {
            return res.status(404).json({ message: 'Store not found' });
        }
        res.json({ name: store.name });
    } catch (err) {
        res.status(500).json({ message: 'Server error' });
    }
});

module.exports = router;