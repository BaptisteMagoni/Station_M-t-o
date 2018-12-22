#!/usr/bin/python3.6
#coding: utf-8

import clientThread
import threadVantagePro2
import socket

if __name__ == "__main__":
    ThreadTrame = threadVantagePro2.threadVantagePro2(demo=True)
    ThreadServer = clientThread.clientThread(VantagePro=ThreadTrame)

    ThreadTrame.start()
    ThreadServer.start()
