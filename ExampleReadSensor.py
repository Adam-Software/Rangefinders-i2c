from rangefinders_i2c.ReadSensor import ReadSensor


class ExampleReadSensor:

    @staticmethod
    def ReadSensorHex():
        sensor = ReadSensor(1)

        try:
            while True:
                for address in range(0x18, 0x1e):
                    distance = sensor.GetDistance(address)
                    print("address:", address, "distance:", distance)
                print("-----------------------------")

        except KeyboardInterrupt:
            sensor.CloseSMBus()
        print("Stopped")

    @staticmethod
    def ReadSensorInt():
        sensor = ReadSensor(1)

        try:
            while True:
                for address in range(24, 30):
                    distance = sensor.GetDistance(address)
                    print("address:", address, "distance:", distance)
                print("-----------------------------")

        except KeyboardInterrupt:
            sensor.CloseSMBus()

        print("Stopped")


if __name__ == "__main__":
    ExampleReadSensor.ReadSensorHex()
    ExampleReadSensor.ReadSensorInt()
