import qwiic
import qwiic_joystick
import time
import sys
import subprocess as sp

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

if myJoystick.connected == True:
	useJoystick = True
	myJoystick.begin()

print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("Time to dance!")
time.sleep(1)

while True:

	if useJoystick:
		x = myJoystick.horizontal
		y = myJoystick.vertical
		b = myJoystick.button

		sp.call('cls',shell=True)
		if x > 575:
			print(" o _") 
			print(" /\\")  
			print(" / |") 
			continue

		elif x < 450:
			print(" _ o") 
			print("  /\\") 
			print(" | \\") 
			continue

		else:
                	x = 0

		if y > 575:
			print("\\ o /")
			print("  |  ")
			print(" / \\") 
			continue

		elif y < 450:
			print("     ")
			print(" o/__") 
			print(" |  (\\")
			continue

		else:
			y = 0

		if x == 0 and y == 0:
			print("  o ")
			print(" /|\\")
			print(" / \\")


