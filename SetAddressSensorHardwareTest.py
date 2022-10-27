from rangefinders_i2c.SensorManagment import SensorManagment


class SetAddressSensorHardwareTest:

    @staticmethod
    def GetUsbDevices():
        sensor = SensorManagment()
        sensor.GetUsbDeviceList()


if __name__ == '__main__':
    SetAddressSensorHardwareTest.GetUsbDevices()
