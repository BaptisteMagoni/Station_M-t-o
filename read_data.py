#!/usr/bin python3.6
#-*-coding: utf-8-*-

from paquet_loop2 import paquet_loop2
from paquet_loop import paquet_loop
from Emulator import Emulator
import ASCII

class Trame:
    
    def __init__(self, trame="Aucune Trame", demo=False, sql=None):
        self.demo = demo
        self.m_trame = trame
        self.list_trame = {}
        self.add_list()
        self.instance_packet = None
        m_type = self.get_type_packet()
        if m_type == "LOOP":
            self.instance_packet = paquet_loop(trame=self.list_trame)
        elif m_type == "LOOP2":
            self.instance_packet = paquet_loop2(trame=self.list_trame)
        if not self.demo:
            self.sql = sql
            self.tuple_list = (str(self.m_trame), str(self.instance_packet.get_type()), str(self.instance_packet.get_bar_trend()), str(self.instance_packet.get_barometer()), str(self.instance_packet.get_inside_temperature()), str(self.instance_packet.get_inside_humidity()), str(self.instance_packet.get_outside_temperature()), str(self.instance_packet.get_wind_speed()), str(self.instance_packet.get_wind_direction()))
            self.sql.insert_data(self.tuple_list)
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

    def get_data_trame(self):
        return self.instance_packet

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