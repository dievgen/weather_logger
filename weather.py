import serial
import datetime
import time
import os
import sys


ser = serial.Serial('COM3', 600)
ser.flushInput()
ser.close()
ser.open()
ts = time.time()
filename = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S_log')
myfile = open(filename+'.csv','w')
#myerrorlog = open('err'+filename+'.log','w')

while 1:
	while(ser.inWaiting()==0):
		pass
	pressure = tempbmp080=tempDHT=tempDS=humidDHT=0
	myfile = open(filename+'.csv','a')
	ts = time.time()
	datestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y/%m/%d')
	timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

	buffer = ser.readline()
	comdata = buffer[2:28]
	strdata = str(comdata)
	comdataA = strdata.split(',')
	try:
		pressure = str(comdataA[0])
		tempbmp080 = str(comdataA[1])
		tempDS = str(comdataA[2])
		tempDHT = str(comdataA[3])
		humidDHT = str(comdataA[4])
		#COsensor = str(comdatA[5])
	except:
		pass

	myfile.write(datestamp+';'+timestamp+';'+pressure+';'+tempDHT+';'+humidDHT+'\n')
	print(datestamp+'/'+timestamp+','+pressure+','+tempDHT+','+tempDS+','+tempbmp080+','+humidDHT)
	myfile.close()