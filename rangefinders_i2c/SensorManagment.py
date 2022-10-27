#!/usr/bin/env python
# -*- coding: utf-8 -*-
import usb.core
import sys
from pickle import TRUE

import serial
from loguru import logger


class SensorManagment:
    def __init__(self, usbAddress='/dev/ttyUSB0', speed=9600):
        self._ser = serial.Serial(usbAddress, speed)
        logger.add('rangefinders.log', retention="10 days", level="INFO")

    # command for change address s7-xxx# - where 'xxx' is your address,
    # not more than 254 (my address is 49,50,52,54,56,58)
    # ser.write(b'r7#') #command for check address
    def setAddress(self, address: int):
        if self._checkAddress(address):
            try:
                raise ValueError
            except ValueError:
                logger.error('Address must be 49, 50, 52, 54, 56, 58')

        self._ser.write(f"'b's7-{address}#'")

        while TRUE:
            message = self._ser.readline()
            logger.info(message)

        self._ser.close()
        logger.info('Sensor write address finish. Serial close')

    def GetUsbDeviceList(self):
        dev = usb.core.find(find_all=True)
        # loop through devices, printing vendor and product ids in decimal and hex

        for cfg in dev:
            try:
                print(
                    'Decimal VendorID=' + str(cfg.idVendor) +
                    ' & ProductID=' + str(cfg.bDeviceClass) +
                    '  ' + str(cfg.product) + ' ' + str(cfg.bDeviceSubClass) +
                    '  ' + str(cfg.manufacturer) + '\n')
            except:
                print('Error read usb')

    @staticmethod
    def _checkAddress(address: int) -> bool:
        if address not in [49, 50, 52, 54, 56, 58]:
            return False

        return True
