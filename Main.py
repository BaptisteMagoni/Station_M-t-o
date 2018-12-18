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
        while 1:
            sleep(1)
            ans = self.serialwrapper.read()
            print(ans)
            #if(len(ans)) == 99:
            #    print("------------------------------------------------------------------------------------------------")
            #    print("Trame : {}".format(ans))
            #    print("Taille de la chaine est de {} donc elle est correct".format(len(ans)))
            #    self.m_trame = Trame(trame=ans, demo=self.demo)
            #    self.m_trame.__del__()
            #    print("------------------------------------------------------------------------------------------------")
            #else:
            #    print("Taille de la chaine est de {} donc elle est pas correct".format(len(ans)))


if __name__ == "__main__":
    Main(demo=False)