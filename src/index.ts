import express from 'express';

// basic api setup

const app = express();
const port = 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello, world!');
});

app.get('/ping', (req, res) => {
  // i can only return one response to the client
  // but i can execute code after the return
  res.send("fff");
  console.log("hallo das ist cool!");

});

// on change of the website playlist
app.post('/suggestion', (req, res) =>{
  // getting the songs

  // converting the songs in the playlist to v

  // searching for a fitting one in the db with magic i wont tell

  // responding with the fitting songs



});

app.post('/data', (req, res) => {
  // the response of the server is still not reachable 
  // something with the setup of the server side script 

  const data = req.body;
  res.send(`You sent: ${data}`);
  // res.send(`You sent: ${JSON.stringify(data)}`);
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
