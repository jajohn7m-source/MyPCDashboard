# MyPCDashboard
Processing onboard system data using Python as the backend data manager and using Node.js to server a front end index.html / script.js / style.css to display the data in real time. 

# Node.js Dependencies
Please make sure you install Node.js on your system otherwise you will run into errors. 

** Presuming you have node.js installed on your pc make sure you have the package.json file which should come with this repo. 

Run the below command in command prompt or terminal (depending on your operating system).

--> npm install express 

--> npm install socket.io


# Python Dependencies (Python Version: 3.10.6)

Run the below command in command prompt or terminal (depending on your operating system). 

--> pip install psutil gputil requests pysensors py3nvml

I have matched up the imports to the above command for a high level overview:

# Imports
import sensors -------> pysensors --------------------> handles some onboard sensor

import psutil --------> psutil -----------------------> Used to get CPU Usage, CPU Temp, nvme temp, RAM Usage

import py3nvml -------> py3nvml ----------------------> Used to get GPU Temp

import GPUtil --------> gputil -----------------------> Used to set a obect of GPU's and get the GPU Load (Usage)

import subprocess ----> Built into python 3.10.6 -----> Used to start the node server in python

import time ----------> Built into python 3.10.6 -----> Used to rest a moment before re-fetching up-to-date data.

import requests ------> requests ---------------------> Used to take the data and send it to the server. 

# Installation Instructions
I will be working on a .sh and windows installer to automate these steps, but for now you would need to perform all the steps above and also move the folder where you would like to have it stored. The file structure should be:

MyPCDashboard (Parent Directory)

--> client(sub-dir)

------> index.html (html file)

------> script.js (javascript file)

------> style.css (style sheet)

--> data_collector(sub-dir)
------> monitor.py (python file)

--> node_modules (sub-dir)
------> Lots of packages used by Node.js

--> server (sub-dir)
------> index.js (server javascript file)

package.json (json file)

package-lock.json (json file)
