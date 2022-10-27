from rangefinders_i2c.SensorManagment import SensorManagment


class SetAddressSensorHardwareTest:

    @staticmethod
    def GetUsbDevices():
        SensorManagment.GetUsbDeviceList()



if __name__ == '__main__':
    SetAddressSensorHardwareTest.GetUsbDevices()
