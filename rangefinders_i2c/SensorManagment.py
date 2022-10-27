#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sh
import serial

from pickle import TRUE
from loguru import logger


class SensorManagment:
    def __init__(self, usbAddress='/dev/ttyUSB0', speed=9600):
        self._ser = serial.Serial(usbAddress, speed)
        logger.add('rangefinders.log', retention="10 days", level="INFO")

    # command for change address s7-xxx# - where 'xxx' is your address,
    # not more than 254 (my address is 48,50,52,54,56,58)
    # ser.write(b'r7#') #command for check address
    def setAddress(self, address: int):
        if self._checkAddress(address):
            try:
                raise ValueError
            except ValueError:
                logger.error('Address must be 48, 50, 52, 54, 56, 58')

        self._ser.write(f"'b's7-{address}#'")

        while TRUE:
            message = self._ser.readline()
            logger.info(message)

        self._ser.close()
        logger.info('Sensor write address finish. Serial close')

    @staticmethod
    def GetUsbDeviceList():
        print(sh.lsusb())

    @staticmethod
    def _checkAddress(address: int) -> bool:
        if address not in [48, 50, 52, 54, 56, 58]:
            return False

        return True
