#!/usr/bin/python3.6
#coding: utf8

import socket
import threading
import socket

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
            if response.decode("utf-8") == "stop":
                self.isFinish = True
                print("Stop processus")
                self.vantage.isFinish = True
                self.__del__()
            else:
                if response != "":
                    print(response.decode("utf-8"))

    def __del__(self):
        pass