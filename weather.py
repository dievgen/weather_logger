import serial
import datetime
import time
import os


port_number = input('input serial port number: ')
#ser = serial.Serial('COM'+ser_number, 9600)
#ser.flushInput()
#ser.close()
#ser.open()
ts = time.time()

class serial_port:
	def __init__(self):
		try:
			self.port = serial_port.read_port(port_number)
			self.ser = serial.serial_port(
				port = serial_port.read_port(port_number),
				baudrate = 9600,
				parity = serial.PARITY_NONE,
				stopbits = serial.STOPBITS_ONE,
				bytesize = serial.EIGHTBITS,
				timeout = 1
			)
		except SerialException:
			print('error connection')
			os._exit()
	def read_port(self):


#filename = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S_log')
#myfile = open(filename+'.csv','w')
while 1:
	while(ser.inWaiting()==0):
		pass
	pressure = tempbmp080=tempDHT=tempDS=humidDHT=COsensor=""
#	myfile = open(filename+'.csv','a')
	ts = time.time()
	datestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y/%m/%d')
	timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

	buffer = ser.readline()
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