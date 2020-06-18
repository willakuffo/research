import mpu6050
m = mpu6050.mpu6050(0x68)
import math

x,y,z = 0,0,0
while True:
	accel_data =m.get_accel_data()
	x,y,z = accel_data['x'],accel_data['y'],accel_data['z']
	
	#RNA
	xynet = math.sqrt(x**2+y**2)
	rna = math.sqrt(xynet**2+z**2) 
	
	
	print(x,y,z,rna)
	
