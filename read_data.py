#!/usr/bin python3.6
#-*-coding: utf-8-*-

from paquet_loop2 import paquet_loop2
from paquet_loop import paquet_loop
from Emulator import Emulator
import ASCII

class Trame:

    def __init__(self, trame="Aucune Trame", demo=False):
        self.demo = demo
        self.m_trame = trame
        self.m_size_type_paquet = 5
        self.list_trame = {}
        self.add_list()
        type = self.get_type_packet()
        if type == "LOOP":
            paquet_loop()
        elif type == "LOOP2":
            paquet_loop2()
        for octect in self.list_trame:
            print(ASCII.getCharacter(self.list_trame[octect]))
        if self.demo:
            self.emulator = Emulator()

    def add_list(self):
        nb_tour = 0;
        etape = 0
        for case in self.m_trame:
            if etape % 2:
                self.list_trame[nb_tour] += case
                nb_tour += 1
                etape = 0
            else:
                self.list_trame[nb_tour] = case
                etape += 1

    def get_type_packet(self):
        if self.list_trame[4] == "00":
            return "LOOP"
        elif self.list_trame[4] == "01":
            return "LOOP2"
        else:
            return "Erreur"

    def __del__(self):
        pass