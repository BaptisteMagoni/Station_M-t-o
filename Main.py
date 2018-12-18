#!/usr/bin/python3.6
#coding: utf-8

from SerialWrapper import SerialWrapper
from read_data import Trame
from time import sleep

class Main:

    def __init__(self, demo=False):
        self.demo = demo
        self.serialwrapper = SerialWrapper(com_str="/dev/ttyUSB0", demo=demo)
        self.serialwrapper.write("LPS\n")
        self.ans = self.serialwrapper.read()
        self.showLastTrame()
            #if(len(ans)) == 99:
            #    print("------------------------------------------------------------------------------------------------")
            #    print("Trame : {}".format(ans))
            #    print("Taille de la chaine est de {} donc elle est correct".format(len(ans)))
            #    self.m_trame = Trame(trame=ans, demo=self.demo)
            #    self.m_trame.__del__()
            #    print("------------------------------------------------------------------------------------------------")
            #else:
            #    print("Taille de la chaine est de {} donc elle est pas correct".format(len(ans)))

    def showLastTrame(self):
        self.byte_afficherBytearrayHexa(self.ans, "-")

    def byte_afficherBytearrayHexa(self, tableOctet, separateur=' '):
        for idx, octet in enumerate(tableOctet):
            if idx != len(tableOctet) - 1:
                print("%s%s" % ('{:02x}'.format(octet), separateur), end='')
            else:  # évite d'afficher le séparateur après le dernier octet affiché
                print('{:02x}'.format(octet))

if __name__ == "__main__":
    Main(demo=False)