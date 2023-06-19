const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Serve the index.html file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../client/index.html'));
});

// Serve the script.js file with the correct MIME type
app.get('/script.js', (req, res) => {
  res.sendFile(path.join(__dirname, '../client/script.js'), {
    headers: {
      'Content-Type': 'application/javascript'
    }
  });
});

app.post('/', express.json(), (req, res) => {
  console.log("SERVER: ")
  const data = req.body;
  console.log(data)
  io.emit('data', data);
  res.sendStatus(200);
});

server.listen(3000, () => {
  console.log('Server is running on port 3000');
});
