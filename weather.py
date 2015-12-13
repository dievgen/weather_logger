import serial
import datetime
import time
import os


number = input('input serial port number: ')
#ser = serial.Serial('COM'+ser_number, 9600)
#ser.flushInput()
#ser.close()
#ser.open()
ts = time.time()

class Serial_port:
	def __init__(self, port, baudrate = 9600, timeout = 5):
		self.port = serial.Serial(
			port = 'COM'+number,
			baudrate = baudrate,
			timeout = timeout,
			writeTimeout=timeout)

	def open(self):
		if(self.port.isOpen() == False):
			self.port.open()
		else:
			self.port.close()
			self.port.open()

	def close(self):
		self.port.close()

	def recvline(self):
		return self.port.readline()

Serial_port(number)
Serial_port(number).open()

#filename = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S_log')
#myfile = open(filename+'.csv','w')
while 1:
	#while(Serial_port(number).inWaiting()==0):
	#	pass
	pressure = tempbmp080=tempDHT=tempDS=humidDHT=COsensor=""
#	myfile = open(filename+'.csv','a')
	ts = time.time()
	datestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y/%m/%d')
	timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

	buffer = Serial_port(number).recvline()
	comdata = buffer[2:35]
	strdata = str(comdata)
	comdataA = strdata.split(',')
	try:
		pressure = comdataA[0]
		tempbmp080 = comdataA[1]
		tempDS = comdataA[2]
		tempDHT = comdataA[3]
		humidDHT = comdataA[4]
		COsensor = comdataA[5]
	except:
		pass
	output = '%s/%s,%s,%s,%s,%s,%s,%s' %(datestamp,timestamp,pressure,tempbmp080,tempDS,tempDHT,humidDHT,COsensor)
#	myfile = open(filename+'.csv','a')
#	myfile.write(str(output))
	print(str(output))
#	myfile.close()
#	Serial_port(number).close()