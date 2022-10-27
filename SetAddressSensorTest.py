import unittest

from rangefinders_i2c.SensorManagment import SensorManagment


class SetAddressSensorTest(unittest.TestCase):

    def testCheckAddress(self):
        self.assertEqual(SensorManagment._checkAddress(5), False)
        self.assertEqual(SensorManagment._checkAddress(11), False)
        self.assertEqual(SensorManagment._checkAddress(49), True)
        self.assertEqual(SensorManagment._checkAddress(50), True)
        self.assertEqual(SensorManagment._checkAddress(52), True)
        self.assertEqual(SensorManagment._checkAddress(54), True)
        self.assertEqual(SensorManagment._checkAddress(56), True)
        self.assertEqual(SensorManagment._checkAddress(58), True)


if __name__ == '__main__':
    unittest.main()
