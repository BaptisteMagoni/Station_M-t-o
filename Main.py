#!/usr/bin/python3.6
#coding: utf-8

from SerialWrapper import SerialWrapper
from read_data import Trame
from time import sleep

class Main:

    def __init__(self, demo=False):
        self.demo = demo
        self.serialwrapper = SerialWrapper(com_str="COM4", demo=demo)
        while 1:
            sleep(1)
            ans = self.serialwrapper.read()
            if(len(ans)) == 198:
                print("Trame : {}".format(ans))
                print("Taille de la chaine est de {} donc elle est correct".format(len(ans)))
                self.m_trame = Trame(trame=ans, demo=self.demo)
                self.m_trame.__del__()
                break
            else:
                print("Taille de la chaine est de {} donc elle est pas correct".format(len(ans)))


if __name__ == "__main__":
    Main(demo=False)