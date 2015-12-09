import serial
import datetime
import time

ser = serial.Serial('COM7', 9600)
ser.flushInput()
ser.close()
ser.open()
ts = time.time()
filename = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S_log')
myfile = open(filename+'.csv','w')
while 1:
	while(ser.inWaiting()==0):
		pass
	pressure = tempbmp080=tempDHT=tempDS=humidDHT=COsensor=""
	myfile = open(filename+'.csv','a')
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
	myfile = open(filename+'.csv','a')
	myfile.write(str(output))
	print(str(output))
	myfile.close()