from pickle import TRUE
import serial

ser=serial.Serial('/dev/ttyUSB0', 9600)
ser.write(b's7-49#') #command for change address s7-xxx# - where 'xxx' is your address, not more than 254 (my address is 49,50,52,54,56,58)
#ser.write(b'r7#') #command for check address

while TRUE:
  readedText = ser.readline()
  print(readedText)

ser.close()