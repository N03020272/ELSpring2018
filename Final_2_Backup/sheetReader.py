import json
import os
import sys
import time
import datetime
import gspread
import OpenSSL
from oauth2client.service_account import ServiceAccountCredentials

os.system("chmod a+x /home/pi/Desktop/ELSpring2018/CodeEmbeddedFinal/sensor_interface")
os.system("/home/pi/Desktop/ELSpring2018/CodeEmbeddedFinal/./sensor_interface")

#static variable for easy usage
txt_files = [f for f in os.listdir('.') if f.endswith('.json')]
if len(txt_files) != 1:
	raise ValueError('Should only be one JSON file here, found several')
filename = txt_files[0]

GDOCS_OAUTH_JSON = filename

#static variable for easy usage
GDOCS_SPREADSHEET_NAME = 'Pi1'

#how fast Google spreadsheets will be receiving data from Pi
FREQUENCY_SECONDS = 4

def login_open_sheet(oauth_key_file, spreadsheet):
	try:
		json_key = json.load(open(GDOCS_OAUTH_JSON))
		scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
		credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
		gc = gspread.authorize(credentials)
		
		worksheet = gc.open(spreadsheet).get_worksheet(1)
		return worksheet
	except Exception as ex:
		print('unable to login and obtain spreadsheet. Check OAuth credentials, sheet name, and the sheet is shared with the client_email.')
		print('Google SpreadSheet login failed with error:', ex)
		sys.exit(1)
		

print('Logging sensor measurements to {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
print('Ctrl-C to exit.')
worksheet = None
while True:

	if worksheet is None:
		worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)
		print('opened sheet')
	
	f = open("readings.txt", "r")
	tempC = int(f.readline())
	humidity = int(f.readline())
	tempF = (int(tempC) * (9/5)) + 32
	date = str(datetime.datetime.now())
	data = []
	data.append(date)
	data.append(tempF)
	data.append(tempC)
	data.append(humidity)
	try:
		worksheet.append_row((data[0], data[1], data[2], data[3]))
	except:
		print('Append error, login retry')
		worksheet = None
		time.sleep(FREQUENCY_SECONDS)
		continue
		
	print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
	time.sleep(FREQUENCY_SECONDS)
