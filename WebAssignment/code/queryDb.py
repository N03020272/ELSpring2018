import sqlite3 as mydb
from flask import Flask, render_template
app = Flask(__name__)

conn = mydb.connect('/home/pi/EL_Projects/ELSpring2018/WebAssignment/code/tempReadings.db')

year = sys.argv[1]
month = sys.argv[2];
day = sys.argv[3];

with conn:
	conn = mydb.connect('tempReadings.db')
	c = conn.cursor()
	cursor = c.execute('SELECT * FROM tempReadings')
	tempReadings = cursor.fetchall()
	
	return tempReadings