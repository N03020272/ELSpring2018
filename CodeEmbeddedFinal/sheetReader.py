##This program will call the sensor to collect data, open the spreadsheet, and insert the data
###
###
import json
import os
import sys
import time
import datetime
import gspread
import OpenSSL
from oauth2client.service_account import ServiceAccountCredentials

#sets permissions for the sensor reading C code
os.system("chmod a+x /home/pi/CodeEmbeddedFinal/sensor_interface")



#searches the directories within the current directory to locate the name of the .json file to store into variable
txt_files = [f for f in os.listdir('.') if f.endswith('.json')]
if len(txt_files) != 1:
	raise ValueError('Should only be one JSON file here, found several')
filename = txt_files[0]
GDOCS_OAUTH_JSON = filename

#Title of the spreadsheet collective
GDOCS_SPREADSHEET_NAME = 'Pi1'

#how fast Google spreadsheets will be receiving data from Pi
FREQUENCY_SECONDS = 5

#Checking access to Google sheets using the json as a key
def login_open_sheet(oauth_key_file, spreadsheet):
	try:
		scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
		credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
		gc = gspread.authorize(credentials)
		worksheet = gc.open(spreadsheet).get_worksheet(2)
		return worksheet
	#if key is not found error exception thrown	
	except Exception as ex:
		print('unable to login and obtain spreadsheet. Check OAuth credentials, sheet name, and the sheet is shared with the client_email.')
		print('Google SpreadSheet login failed with error:', ex)
		sys.exit(1)
print('Ctrl-C to exit.')
worksheet = None
#Once access is checked, the sheet is accessed and data is manipulated then written to a row on the sheet
while True:
	if worksheet is None:
		#using method above with json credentials, Google sheets is opened 
		worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)
		print('opened sheet')
	#reading in the temperature values from the values from the sensor stored by the C code	
	#Activates the sensor which reads the temperature and humidity
	os.system("/home/pi/CodeEmbeddedFinal/./sensor_interface")
	f = open("readings.txt", "r")
	tempC = int(f.readline())
	print (tempC)
	humidity = int(f.readline())
	print (humidity)
	tempF = ((tempC) * (9/5) + 32)
	date = str(datetime.datetime.now())
	data = [date,tempF,tempC,humidity]
	try:
	    #writing the data to the row in the spreadsheet
		worksheet.append_row((data[0], data[1], data[2], data[3]))
	except:
	    #if there was an error whether typing or syntax error message thrown and attempt to restart the login and re-write the row
		print('Append error, login retry')
		worksheet = None
		time.sleep(FREQUENCY_SECONDS)
		continue
		
	print('Row written.')
	#delay that controls how fast the pi uploads data to the spreadsheet
	time.sleep(FREQUENCY_SECONDS)
