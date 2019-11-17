import serial
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="moikkajee",
  database="liikennevalot"
)
valot = []
cursor = mydb.cursor()

def kirjoitaTauluun(data):
    if str(data)[2] == "P":
        valot = [1, 0, 0]

    if str(data)[2] == "V":
        valot = [0, 0, 1]
    
    if str(data)[2] == "K":
        valot = [0, 1, 0]

    
    sql = "UPDATE valot SET punainen = " + str(valot[0]) + ", keltainen = " + str(valot[1]) + ", vihrea = " + str(valot[2]) + " WHERE id = 1;"
    cursor.execute(sql)
    mydb.commit()


arduino = serial.Serial('/dev/cu.usbserial-DN04MSTR', 9600, timeout=.1)
while True:
	data = arduino.readline() #the last bit gets rid of the new-line chars
	if data:
		kirjoitaTauluun(data)