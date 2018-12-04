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
            print("Création de la méthode Sérial Wrapper")
            if com_port is not None:
                self.ser = serial.Serial('COM{}'.format(com_port), 9600, timeout=20, stopbits=2, dsrdtr=True)
                print("COM PORT {} trouvé !".format(com_port))
            elif com_str is not None:
                self.ser = serial.Serial(com_str, baudrate=9600, timeout=0)
        else:
            print("Mode démo")

    def write(self, data):
        if not self.demo:
            print("Ecriture {}".format(data))
            self.ser.write(data.encode())
            self.ser.flush()

    def read(self):
        if not self.demo:
            try:
                return self.ser.read(size=198).decode('utf-8')
            except:
                self.log.error("Un erreur c'est produite dans la lecture du port série !")
        else:
            return "4c4f4f1401ff7f0275d40224b90104ff3b014a003c0010005101ff7fff7f2100ff41ff2b002800ff000000ffff7f0c0092240c000000000000000c00020000ffff027502750275ff00050e120a06151e030101ff7fff7fff7fff7fff7fff7f0a0d40c0"
