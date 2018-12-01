#!/usr/bin/python3.6
#coding: utf-8

import serial
import serial.tools.list_ports
import logging
from Emulator import Emulator

class SerialWrapper:

    def __init__(self, com_port=None, com_str=None, demo=False):
        self.demo = demo
        if not self.demo:
            self.log = logging.getLogger(__name__)
            print("MySerialVisaWrapper instance created")
            if com_port is not None:
                self.ser = serial.Serial('COM{}'.format(com_port), 9600, timeout=20, stopbits=2, dsrdtr=True)
                self.log.info("COM PORT Found !")
                print("COM PORT {} Found !".format(com_port))
            elif com_str is not None:
                self.ser = serial.Serial(com_str, baudrate=9600, timeout=0)
        else:
            self.emulator = Emulator()

    def write(self, data):
        if not self.demo:
            print("MySerialVisaWrapper Writing {}".format(data))
            self.ser.write(data.encode())
            self.ser.flush()
        else:
            self.protocolDecoder.protocol_decoder(data)

    def read(self):
        try:
            return self.ser.read(size=198).decode('utf-8')
        except:
            self.log.error("Un erreur c'est produite dans la lecture du port série !")
