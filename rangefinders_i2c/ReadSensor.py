#!/usr/bin/env python
# -*- coding: utf-8 -*-

from smbus2 import SMBus
from loguru import logger


class ReadSensor:
    _bus = None

    def __init__(self,
                 i2sAddress: int,
                 loggerVerbose=False):

        if loggerVerbose is True:
            logger.remove()

        logger.add('rangefinders.log', retention="10 days", level="ERROR")

        self._bus = SMBus(i2sAddress)

    def GetDistance(self, address):
        try:
            self._bus.write_byte(address, 0)
            distance = self._bus.read_byte(address) << 8 | self._bus.read_byte(address)
            return distance

        except IOError:
            logger.error('i2c address does not exist or rangefinder not connected')
            pass

    def CloseSMBus(self):
        try:
            self._bus.close()

        except IOError:
            logger.error('SMBus not open')
            pass
