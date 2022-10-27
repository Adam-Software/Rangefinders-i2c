# Rangefinders-i2c

### What the library can do?
1. Change TOF10120 address device by usb. 
2. Get data from TOF10120 device by i2c

### How install
```commandline
pip install rangefinders-i2
```

## Change address

To change the address, a usb programmer is needed.
After connecting the programmer, you can find out the address using the following code


if your programmer is the only device (connect to /dev/ttyUSB0)
```python
from rangefinders_i2c.SensorManagment import SensorManagment

managment = SensorManagment()
```
if there is more than one device, then you can find it using the following code
```python
print(SensorManagment.GetUsbDeviceList())
```
and by selecting a device, you can specify it when initializing an instance of the class
```python
managment = SensorManagment('/dev/ttyUSB1')
```
the second parameter is the port speed, by default it is 9600. To change the speed, use the second parameter when initializing the class instance
```python
managment = SensorManagment('/dev/ttyUSB1', 4800).
```
After that, you should call the function `setAddress`
```python
managment = SensorManagment()
managment.setAddress(48)
```
for all rangefinders, we use constant values: 48, 50, 52, 54, 56, 58.

Calling the set Address() function with a value other than the specified constants will result in an error: ValueError('Address must be 48, 50, 52, 54, 56, 58')

## Get Data from TOF10120

In order to get the values, you should initialize an instance of the class

```python
from rangefinders_i2c.ReadSensor import ReadSensor

sensor = ReadSensor(1)
```
where 1 is the smbus bus number.

You can also enable verbose mode (log error to console) using the following code
```python
sensor = ReadSensor(1, True)
```

After that, you can get the value from the device by passing it the address as a parameter

```python
address = 0x18
distance = sensor.GetDistance(address)
print("address:", address, "distance:", distance)
```

or

```python
address = 24
distance = sensor.GetDistance(address)
print("address:", address, "distance:", distance)
```





