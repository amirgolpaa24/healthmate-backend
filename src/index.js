require('dotenv').config();
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const morgan = require('morgan');

const app = express();
const PORT = process.env.PORT || 8000;

app.use(express.json());
app.use(helmet());
app.use(cors());
app.use(morgan('dev'));

app.get('/', (req, res) => res.json({ msg: 'HealthMate backend is live!' }));

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
