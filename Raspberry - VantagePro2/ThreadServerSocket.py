import time
import sys
import binascii
import socket
from threading import Thread
import pymysql

class ThreadServerSocket(Thread):
   def __init__(self, host, port, ThreadVP2):
      Thread.__init__(self)
      self.ThreadVP2 = ThreadVP2
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.sock.bind((host, port))
      self.connection = pymysql.connect(host='10.6.0.1', user='meteo', password='Nantes44', db='meteo', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

   def run(self):
      while True:
         try:
            print('Waitting for client...')
            self.sock.listen(5)
            client, address = self.sock.accept()
            print ("{} connected".format(address))

            response = client.recv(255)
            if response != "":
               #print(response)
               try:
                  client.sendall(self.ThreadVP2.getLastTrame())
                  with self.connection.cursor() as cursor:
                     ip, port = address
                     sql="INSERT INTO `meteo`.`log` (`id`, `date_heure`, `message`) VALUES (NULL, NOW(), 'Connexion socket de " + str(ip) + "');"
                     cursor.execute(sql)
                     self.connection.commit()
               except ValueError:
                  print("Impossible d'enregistrer le log");
         except ValueError:
            print("Erreur serveur socket");
            try:
               with self.connection.cursor() as cursor:
                  ip, port = address
                  sql="INSERT INTO `meteo`.`log` (`id`, `date_heure`, `message`) VALUES (NULL, NOW(), 'Erreur serveur socket');"
                  cursor.execute(sql)
                  self.connection.commit()
            except ValueError:
               print("Impossible d'enregistrer le log");
