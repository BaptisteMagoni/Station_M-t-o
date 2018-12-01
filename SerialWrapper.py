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

    def write(self, data):
        if not self.demo:
            print("MySerialVisaWrapper Writing {}".format(data))
            self.ser.write(data.encode())
            self.ser.flush()

    def read(self):
        if not self.demo:
            try:
                return self.ser.read(size=198).decode('utf-8')
            except:
                self.log.error("Un erreur c'est produite dans la lecture du port série !")
        else:
            return "4c4f4f1401ff7f0375d40225c20105ff57013c00580010005101ff7fff7f2000ff3dff2c002900ff000000ffff7f0c0092240c000000000000000c00020000ffff037503750375ff06050e120a02151a030101ff7fff7fff7fff7fff7fff7f0a0d5ea0"
