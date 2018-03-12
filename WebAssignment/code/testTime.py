from flask import Flask, render_template
from flask.json import jsonify
import datetime
import sqlite3 as mydb
app = Flask(__name__)



@app.route("/")
def index():
	now = datetime.datetime.now()
	timestring = now.strftime("%Y-%m-%d  %H:%M:%S")
	firstSplit = timestring.split(" ")
	dbItems1 = firstSplit[0].split("-")
	dbItems2 = firstSplit[1].split(":")
	dbItems = dbItems1 + dbItems2
	
	conn = mydb.connect('tempReadings.db')
	c = conn.cursor()
	cursor = c.execute('SELECT * FROM tempReadings')
	
	
	# with conn:
	  
		# cur = conn.cursor()
		# cur.execute("select * from tempReadings")
		# data = cur.fetchone()
		# #print "SQLite version: %s" % data
		
	# templateData = {
		# 'time' : timestring,
		# 'data' : items
	# }
	
	return render_template('index.html', tempReadings = cursor.fetchall())
	
	
@app.route("/temp/<year1>/<year2>/<month1>/<month2>/<day1>/<day2>", methods=['GET'])
def selectRange(year1, year2, month1, month2, day1, day2):
	conn = mydb.connect('tempReadings.db')
	c = conn.cursor()
	dateParams = [year1 , year2 , month1 , month2 , day1 , day2]
	cursor = c.execute('SELECT * FROM tempReadings WHERE year BETWEEN ? AND ? AND month BETWEEN ? AND ? AND day BETWEEN ? AND ?', dateParams)
	tempReadings = cursor.fetchall()
	print tempReadings
	#return jsonify(tempReadings)
	return jsonify(data = tempReadings)
	#return render_template('index.html', tempReadings = cursor.fetchall())
	
@app.route("/temperature")
def temperature():
	templateData = {
		'data' : "yeh"
	}
	return render_template('temperature.html', **templateData)

	

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)
	