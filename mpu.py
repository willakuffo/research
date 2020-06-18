import mpu6050
m = mpu6050.mpu6050(0x68)
import math

ax,ay,az = 0,0,0
gravity = 9.81

def linear_acc():
	'''calc linear acc in 2d xy plane'''
	#expected acc for RNA
	axy= math.sqrt(gravity**2 - az**2)
	return axy
	
	
	
	
	
while True:
	accel_data =m.get_accel_data()
	ax,ay,az = accel_data['x'],accel_data['y'],accel_data['z']
	
	#RNA
	xynet = math.sqrt(ax**2+ay**2)
	rna = math.sqrt(xynet**2+az**2) 
	
	
	#print(ax,ay,az,rna)
	print(linear_acc())
