# FINAL PROJECT README AND INSTRUCTIONS: 
 
 __Goals:__
 
  -To make a modular, extendable, automatic temperature and humidity data logging device. 
 
 -To create system to be able to store the data collected into a central locaton, which in our case was google spreadsheet.
 
 -To develop a driver for interfacing with the sensor itself using C code.
 
 -To write python code to interface with the google sheet api using several downloaded librarires and a JSON, Service Account Key.
  
 __Work Division__
 
  Joe Adamczyk: 33.3% ---> Sensor Driver and 3D printing
  
  Jonathan Bing: 33.3% --> Pi to google spreadsheet scripts and seemless extension
  
  Joseph Echeverria: 33.3% --> Web interface
  
  Chikkaral Easwarren: .01% :)
  
 
 __Achievements:__
  
  -Made 3d printed boxes for the units
  
  -Made a modular and extendable temperature sensor system
  
  -Made a google sheet-based database system for logging data
  
  -Made scripts to log and send data to the sheets
  
  -Made a web interface for displaying the data
  
  -Made a driver for the one-wire serial temperature and humidity sensor
 
 
 __Instructions:__
 
 1. Download the necessary code from the repository 
 
 2. Run setup.py to download the necessary libraries
 
 3. Load web interface code into visual studios or another web design IDE
 
 4. Run "ng serve". Which will compile and host the site locally
 
 5. In order to make the website use the new pi's data in the charts you have to copy the "GID" number from the URL of the sheet and paste it into "index.html" -> "draw chart" -> "GidNum" variable....If further guidance needed refer to install tab on the webpage
  
