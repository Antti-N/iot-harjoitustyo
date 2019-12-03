import serial
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
  host="localhost",
  user="iot",
  passwd="password",
  database="liikennevalot"
)

cursor = db.cursor()

def deleteFrontRows():
	cursor.execute("DELETE FROM ilma ORDER BY id LIMIT 1")
	db.commit()

def count():
	cursor.execute("SELECT COUNT(*) FROM ilma")
	return cursor.fetchone()

def writeTempAndHum(data):
	
	if count()[0] > 20:
		deleteFrontRows()
	now = datetime.now()

	curTime = now.strftime("%H:%M:%S")
	
	val = (curTime, float(data[0]), float(data[1]))
	
	sql = "INSERT INTO ilma (aika, lampo, kosteus) VALUES (%s, %s, %s)"
	cursor.execute(sql, val)
	db.commit()


arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=.1)

while True:
	data = arduino.readline() #the last bit gets rid of the new-line chars
	
	if data:
		if data[0] == 'P' or data[0] == 'K' or data[0] == 'V':
			print("Oli valo")
		if data[0] == 'I':
			writeTempAndHum(data[3:].split(","))

