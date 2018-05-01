import time
import smbus

def motor(motor, direction, speed):
	bus.write_byte(0x08, 0x0A)
	bus.write_byte(0x08, 0x55)
	bus.write_byte(0x08, 0x01)
	bus.write_byte(0x08, 0x03)
	bus.write_byte(0x08, motor)
	bus.write_byte(0x08, direction)
	bus.write_byte(0x08, speed)

bus = smbus.SMBus(1)

while True:
	try:
		
		motor(1,1,100)
		motor(2,0,0)
		
		time.sleep(3)
		
		motor(1,0,0)
		motor(2,1,100)
		
		time.sleep(3)
		
		motor(1,2,200)
		motor(2,0,0)
		
		time.sleep(3)
		
		motor(1,2,0)
		motor(2,1,200)
		
		time.sleep(3)
		
		
		motor(1,0,0)
		motor(2,1,0)
		
		time.sleep(3)
		
	except IOError:
		print("NG")