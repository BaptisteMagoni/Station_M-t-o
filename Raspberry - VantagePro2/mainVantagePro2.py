import time
import sys
import serial
import binascii
import socket
import threading
import ThreadServerSocket
import ThreadAcquisitionVantagePro2

if __name__ == "__main__":
   print('Start programme...')
   
   ThreadVP2 = ThreadAcquisitionVantagePro2.ThreadAcquisitionVantagePro2()
   ThreadSrv = ThreadServerSocket.ThreadServerSocket('',1510, ThreadVP2)
   
   ThreadVP2.start()
   ThreadSrv.start()
   