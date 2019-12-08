import serial
import mysql.connector
from datetime import datetime
import pygame
import time

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
	
def writeValot(data):
             
        if data == 1:
            sql = "UPDATE valot SET punainen=0, vihrea=1 WHERE id=1"
        
        if data == 0:
            sql = "UPDATE valot SET punainen=1, vihrea=0 WHERE id=1"
        
        cursor.execute(sql)
        db.commit()


arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=.1)

while True:
	data = arduino.readline() #the last bit gets rid of the new-line chars
		
	if data:
		pygame.mixer.init()
		while data[0] == 'P':
			print("Punainen")
			vihrea = 0
			data = arduino.readline()
			pygame.mixer.music.load("/home/pi/iot-harjoitustyo/aanet/red.wav")
			pygame.mixer.music.play()
		while data[0] == 'V':
                        print("Vihrea")
                        vihrea = 1
			data = arduino.readline()
			pygame.mixer.music.load("/home/pi/iot-harjoitustyo/aanet/green.wav")
			pygame.mixer.music.play()
		if data[0] == 'I':
                        writeTempAndHum(data[3:].split(","))
                        writeValot(vihrea)
