#!/usr/bin/python3.6
#coding: utf-8

import serial
import serial.tools.list_ports
import logging

TRAME = {

}

class SerialWrapper:

    def __init__(self, com_port=None, com_str=None, demo=False):
        self.demo = demo
        self.index = 0
        if not self.demo:
            self.log = logging.getLogger(__name__)
            print("Création de la méthode Sérial Wrapper")
            if com_port is not None:
                self.ser = serial.Serial(port=com_port, baudrate=19200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=5)
                print("COM PORT {} trouvé !".format(com_port))
            elif com_str is not None:
                try:
                    self.ser = serial.Serial(port=com_str, baudrate=19200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=5)
                    print("COM STR {} trouvé !".format(com_str))
                except:
                    print("Erreur COM STR")
        else:
            self.init_trame_dict()
            print("Mode démo")

    def write(self, data):
        if not self.demo:
            print("Ecriture {}".format(data))
            self.ser.write(data.encode())

    def read(self):
        if not self.demo:
            try:
                return self.ser.read(size=198)
            except:
                self.log.error("Un erreur c'est produite dans la lecture du port série !")
        else:
            try:
                trame = TRAME[self.index]
                self.index += 1
                if trame[len(trame)-1] is "\n":
                    return trame[:-1]
                else:
                    return trame
            except:
                self.index = 0


    def init_trame_dict(self):
        i = 0
        fichier = open("trame.txt", "r")
        for ligne in fichier.readlines():
            TRAME[i] = ligne
            i += 1
