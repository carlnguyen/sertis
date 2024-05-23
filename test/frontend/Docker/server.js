'use strict';const express = require('express');
// Constantsconst 
PORT = 8080;
const HOST = '0.0.0.0';
// Appconst
app = express();
app.get('/', (req, res) => {
  res.send('Hello world');
});
app.get('/healthz',(req,res)=> {
  res.send ("Health check passed");
});
app.get('/healthz',(req,res)=> {
  res.status(500).send('Health check did not pass');
});
app.listen(PORT, HOST);
console.log(Running on http://${HOST}:${PORT});
