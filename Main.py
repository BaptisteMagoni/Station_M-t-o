#!/usr/bin/python3.6
#coding: utf-8

from SerialWrapper import SerialWrapper
from read_data import Trame
from time import sleep
import sys

class Main:

    def __init__(self, demo=False):
        try:
            self.demo = demo
            self.serialwrapper = SerialWrapper(com_str="/dev/ttyUSB0", demo=demo)
            self.serialwrapper.write("LPS\n")
            self.ans = self.serialwrapper.read()
            print(self.ans)
            if(len(self.ans)) == 198:
                print("------------------------------------------------------------------------------------------------")
                #print("Trame : {}".format(self.ans))
                #print("Taille de la chaine est de {} donc elle est correct".format(len(self.ans)))
                self.m_trame = Trame(trame=self.ans, demo=self.demo)
                self.m_trame.__del__()
                print("------------------------------------------------------------------------------------------------")
            else:
                print("Taille de la chaine est de {} donc elle est pas correct".format(len(self.ans)))
        except ValueError:
            print("Mettez vous en mode démo ou alors il y a un problème quelque part d'autre !")

    #def showLastTrame(self):
    #    self.byte_afficherBytearrayHexa(self.ans, "-")

    #def byte_afficherBytearrayHexa(self, tableOctet, separateur=' '):
    #    for idx, octet in enumerate(tableOctet):
    #        if idx != len(tableOctet) - 1:
    #            print("%s%s" % ('{:02x}'.format(octet), separateur), end='')
    #        else:  # évite d'afficher le séparateur après le dernier octet affiché
    #            print('{:02x}'.format(octet))

if __name__ == "__main__":
    Main(demo=True)