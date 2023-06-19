#!/bin/sh

# Update the pc
apt-get update

# Install node.js & Node Dependencies
apt-get install nodejs
apt-get install npm

npm install express
npm install socket.io

# Install python & python dependencies
apt-get install python3
apt-get install pip

pip install psutil gputil requests pysensors py3nvml
