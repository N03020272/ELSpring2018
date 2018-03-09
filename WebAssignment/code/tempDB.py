import sqlite3 as mydb
import datetime

conn = mydb.connect('/home/pi/EL_Projects/ELSpring2018/WebAssignment/code/tempReadings.db')

tempfile = open("/sys/bus/w1/devices/28-0000069885c5/w1_slave") 
tempfile_text = tempfile.read() 
tempfile.close()

tempC=[float(tempfile_text.split("\n")[1].split("t=")[1])/1000]

print tempC

now = datetime.datetime.now()
timestring = now.strftime("%Y-%m-%d s %H:%M:%S")
firstSplit = timestring.split("s")
dbItems1 = firstSplit[0].split("-")
dbItems2 = firstSplit[1].split(":")
dbItems = dbItems1 + dbItems2 + tempC

with conn:
  
	cur = conn.cursor()
	cur.execute('INSERT INTO tempReadings VALUES (?,?,?,?,?,?,?)', dbItems)
	data = cur.fetchone()
	

	