#!/usr/bin/python3.6
#coding: utf8

import socket
import threading
import socket
import os
import signal
import threadVantagePro2
DICT_DATA = {
    "GET:TYPEPACKET": "self.vantage.get_instance_trame().get_type_packet()",
    "GET:STRTRAME": "self.vantage.get_instance_trame().get_str_trame()",
    "GET:BARTREND": "self.vantage.get_instance_trame().get_data_trame().get_bar_trend()",
    "GET:BAROMETER": "self.vantage.get_instance_trame().get_data_trame().get_barometer()",
    "GET:INSIDETEMP": "self.vantage.get_instance_trame().get_data_trame().get_inside_temperature()",
    "GET:INSIDEHUMIDITY": "self.vantage.get_instance_trame().get_data_trame().get_inside_humidity()",
    "GET:OUTSIDETEMP": "self.vantage.get_instance_trame().get_data_trame().get_outside_temperature()",
    "GET:WINDSPEED": "self.vantage.get_instance_trame().get_data_trame().get_wind_speed()",
    "GET:WINDDIRECTION": "self.vantage.get_instance_trame().get_data_trame().get_wind_direction()",
    "GET:ALL": "self.vantage.get_instance_trame().get_all_data()",
    "ERROR": "ERROR"
}

class clientThread(threading.Thread):


    def __init__(self, VantagePro=None):
        self.isFinish = False
        self.vantage = VantagePro
        threading.Thread.__init__(self)
        print("Socket server start")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', 55000))

    def run(self):
        while not self.isFinish:
            self.socket.listen(5)
            client, address = self.socket.accept()
            print("{} connected".format(address))

            response = client.recv(255)
            client_send = response.decode("utf-8")
            print("Recu : {}".format(client_send))
            if client_send == "stop":
                self.socket.close()
                client.close()
                self.isFinish = True
                self.vantage.isFinish = True
                self.__del__()
                self.vantage.__del__()
                print("Stop processus")
                if not self.demo:
                    os.kill(os.getpid(), signal.SIGTERM)
            else:
                if response != "":
                    for command in DICT_DATA:
                        if command == client_send:
                            try:
                                data = str(eval(DICT_DATA[command])).encode()
                                client.send(data)
                                print("Envoi de : {}".format(data))
                            except ValueError as err:
                                print("Erreur : {}".format(err))


    def __del__(self):
        pass