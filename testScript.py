import qwiic
import qwiic_joystick
import qwiic_bme280
import qwiic_ccs811
import time
import sys

print()
print()
print("----------")
print("Qwiic I2C Python Demo with Binho Multi-Protocol USB Host Adapter from Win/Mac/Ubuntu")
print("----------")
print()
print("Scanning for Qwiic Devices...")
print()

devices = qwiic.list_devices()

if len(devices) == 0:
	print("No Devices Found!")
	exit(1)

print("Found the following device(s):")
for device in devices:
	print(device[1])


myJoystick = qwiic_joystick.QwiicJoystick()
bme280 = qwiic_bme280.QwiicBme280()
ccs811 = qwiic_ccs811.QwiicCcs811()

if myJoystick.connected == True:
	useJoystick = True
	myJoystick.begin()

if bme280.connected == True:
	useBme280 = True
	bme280.begin()

	bme280.filter = 1  		# 0 to 4 is valid. Filter coefficient. See 3.4.4
	bme280.standby_time = 0 	# 0 to 7 valid. Time between readings. See table 27.
	
	bme280.over_sample = 1			# 0 to 16 are valid. 0 disables temp sensing. See table 24.
	bme280.pressure_oversample = 1	# 0 to 16 are valid. 0 disables pressure sensing. See table 23.
	bme280.humidity_oversample = 1	# 0 to 16 are valid. 0 disables humidity sensing. See table 19.
	bme280.mode = bme280.MODE_NORMAL # MODE_SLEEP, MODE_FORCED, MODE_NORMAL is valid. See 3.3

if ccs811.connected == True:
	useCcs811 = True
	ccs811.begin()



while True:

	if useJoystick:
		x = myJoystick.horizontal
		y = myJoystick.vertical
		b = myJoystick.button

		if x > 575:
			print("Joystick: Left")
		elif x < 450:
			print("Joystick: Right")

		if y > 575:
			print("Joystick: Up")
		elif y < 450:
			print("Joystick: Down")

		if b == 0:
			print("Joystick: Button")

		print()
			
	if useBme280:
		print("Humidity:\t%.3f %%RH" % bme280.humidity)

		print("Pressure:\t%.3f Pa" % bme280.pressure)	

		print("Altitude:\t%.3f feet" % bme280.altitude_feet)

		print("Temperature:\t%.2f degF\n" % bme280.temperature_fahrenheit)

	if useCcs811:
		
		ccs811.read_algorithm_results()

		print("CO2:\t%.3f" % ccs811.CO2)

		print("tVOC:\t%.3f\n" % ccs811.TVOC)	

	time.sleep(.5)