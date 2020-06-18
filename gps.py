'''
Fix serial Exception of multiple or disconnected 
device or empty buffer:
To manually change the settings, edit the kernel command line 
with ---sudo nano /boot/cmdline.txt---. Find the console entry that 
refers to the serial0 device, and remove it, including the baud 
rate setting. It will look something like console=serial0,115200. 
Make sure the rest of the line remains the same, as errors in 
this configuration can stop the Raspberry Pi from booting.

'''


import serial
import pynmea2

gps_identifier = b'$GPGLL'
port = '/dev/ttyS0'
connection = serial.Serial(port,baudrate = 9600)

while True:
	
	raw_data = connection.readline()
	#print(raw_data[:len(gps_identifier)].decode('utf-8'))
		
	if raw_data[0:len(gps_identifier)] == gps_identifier:
		gpsdata = pynmea2.parse(raw_data.decode('utf-8'))
		lat = gpsdata.latitude
		lon = gpsdata.longitude
		print('lat:',lat,'lon:',lon)
	
