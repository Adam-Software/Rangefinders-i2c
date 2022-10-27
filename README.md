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
```commandline
managment = SensorManagment()
```
if there is more than one device, then you can find it using the following code
```commandline
print(SensorManagment.GetUsbDeviceList())
```


