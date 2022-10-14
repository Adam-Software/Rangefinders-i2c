#!/usr/bin/python
import time
from smbus2 import SMBus
#from micropython import const

bus = SMBus(1)
time.sleep(1)
#prev_distance = 200

def range_mm(address):
    try:
      bus.write_byte(address,0)
      time.sleep(0.02)
      value = bus.read_byte(address) << 8 | bus.read_byte(address)
      time.sleep(0.05)
      return value

    except IOError:
      print('i2c address does not exist')
      pass

try:
  while True:
    for adress in range(0x18, 0x1b):
      distance = range_mm(adress)
      print("address:", adress,"distance:", distance)
    
except KeyboardInterrupt:
  bus.close()
print("Stopped")