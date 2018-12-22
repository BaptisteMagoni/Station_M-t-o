#!/usr/bin/python3.6
#coding: utf-8

from SerialWrapper import SerialWrapper
from read_data import Trame
import threading
from time import sleep
from SqlConnection import SqlConnection
import sys

class threadVantagePro2(threading.Thread):

    def __init__(self, demo=False):
        threading.Thread.__init__(self)
        self.isFinish = False
        print("Main Thread start")
        self.demo = demo
        self.m_trame = None
        self.sql = None
        if not self.demo:
            self.sql = SqlConnection(m_host="localhost", m_user="root", m_password="titibaba44", m_database="bdd_station_meteo")
        self.serialwrapper = SerialWrapper(com_str="/dev/ttyUSB0", demo=demo)
        self.serialwrapper.write("LPS\n")

    def run(self):
        while not self.isFinish:
            try:
                self.ans = self.serialwrapper.read()
                print("Trame : {}".format(self.ans))
                if(len(self.ans)) == 198:
                    print("------------------------------------------------------------------------------------------------")
                    self.m_trame = Trame(trame=self.ans, demo=self.demo, sql=self.sql)
                    print("------------------------------------------------------------------------------------------------")
                else:
                    print("Taille de la chaine est de {} donc elle est pas correct".format(len(self.ans)))
            except ValueError:
                print("Mettez vous en mode démo ou alors il y a un problème quelque part d'autre !")
            sleep(5)
        if self.isFinish:
            self.__del__()

    def get_instance_trame(self):
        return self.m_trame

    #def showLastTrame(self):
    #    self.byte_afficherBytearrayHexa(self.ans, "-")

    #def byte_afficherBytearrayHexa(self, tableOctet, separateur=' '):
    #    for idx, octet in enumerate(tableOctet):
    #        if idx != len(tableOctet) - 1:
    #            print("%s%s" % ('{:02x}'.format(octet), separateur), end='')
    #        else:  # évite d'afficher le séparateur après le dernier octet affiché
    #            print('{:02x}'.format(octet))

    def __del__(self):
        pass