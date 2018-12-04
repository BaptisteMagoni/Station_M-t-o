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
        self.list_trame = {}
        self.add_list()
        self.instance_packet = None
        type = self.get_type_packet()
        if type == "LOOP":
            self.instance_packet = paquet_loop(trame=self.list_trame)
        elif type == "LOOP2":
            self.instance_packet = paquet_loop2(trame=self.list_trame)
        print("Bar Trend : {}".format(self.instance_packet.get_bar_trend()))
        print("Barometer : {} inches".format(self.instance_packet.get_barometer()))
        print("Inside temperature : {} °C".format(self.instance_packet.get_inside_temperature()))
        print("Inside Humidity : {} %".format(self.instance_packet.get_inside_humidity()))
        print("Outside Temperature : {} °C".format(self.instance_packet.get_outside_temperature()))
        print("Wind speed : {} km/h".format(self.instance_packet.get_wind_speed()))
        print("Wind direction : {} °".format(self.instance_packet.get_wind_direction()))
        if self.demo:
            self.emulator = Emulator()
        #print(ASCII.getDecimal(self.list_trame[3]))


    def add_list(self):
        nb_tour = 0
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