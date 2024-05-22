import express from 'express';

// generic api setup with express

const app = express();
const port = 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello, world!');
});

app.post('/data', (req, res) => {
  const data = req.body;
  res.send(`You sent: ${JSON.stringify(data)}`);
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});