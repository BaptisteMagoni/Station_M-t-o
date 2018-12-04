import time
import sys
import serial
import binascii
from threading import Thread
from PyCRC.CRCCCITT import CRCCCITT
import pymysql

class ThreadAcquisitionVantagePro2(Thread):
   def __init__(self):
      Thread.__init__(self)
      self.ser = serial.Serial(
         port='/dev/ttyUSB0',
         baudrate = 19200,
         parity=serial.PARITY_NONE,
         stopbits=serial.STOPBITS_ONE,
         bytesize=serial.EIGHTBITS,
         timeout=5
      )
      self.connection = pymysql.connect(host='10.6.0.1', user='meteo', password='Nantes44', db='meteo', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
      #print('Start acquisition LOOP2...')
      serialcmd = 'LPS\n'
      self.ser.write(serialcmd.encode())

   def run(self):
      while True:
         #print('Trame reçue...')
         self.ser.reset_input_buffer()
         self.ser.reset_output_buffer()
         self.lastTrame=self.ser.read(99)
         sys.stdout.flush()
         self.ser.flush()
         #self.showLastTrame()
         
         try:
            if (len(self.lastTrame) != 99):
               raise Exception('La trame ne fait pas 99 octets.')
               
            crcTrame = self.lastTrame[97] * 256 + self.lastTrame[98]
            crcCalcule = CRCCCITT().calculate(self.lastTrame[0:97])
            #print("{:20s} {:10X}".format('CRC-CCITT(XModem)', CRCCCITT().calculate(self.lastTrame)))
            
            if (crcTrame != crcCalcule):
               raise Exception('Erreur de CRC.')
               
            self.decodeTrame()
            self.insertBdd()
            
         except Exception as error:
            print('Exception : ' + str(error))
            #print(self.getTrameStr())
            
            if(len(self.lastTrame) != 99):
               try:
                  with self.connection.cursor() as cursor:
                     sql="INSERT INTO `meteo`.`log` (`id`, `date_heure`, `message`) VALUES (NULL, NOW(), '" + str(error) + "');"
                     
                     cursor.execute(sql)
                     self.connection.commit()
                     
               except ValueError:
                  print("Impossible d'enregistrer la trame");
            
               serialcmd = 'LPS\n'
               self.ser.write(serialcmd.encode())
               
            else:
               try:
                  with self.connection.cursor() as cursor:
                     sql = "INSERT INTO trame (date_heure, trame) VALUES (NOW(), '" + self.getTrameStr() + "');"
                     
                     cursor.execute(sql)
                     self.connection.commit()
                     trame_id = cursor.lastrowid
                     
                     sql="INSERT INTO `meteo`.`log` (`id`, `date_heure`, `message`, `trame_id`) VALUES (NULL, NOW(), '" + str(error) + "', "+str(trame_id)+");"
                     cursor.execute(sql)
                     self.connection.commit()
               except ValueError:
                  print("Impossible d'enregistrer le log");

   def showLastTrame(self):
      self.byte_afficherBytearrayHexa(self.lastTrame, "-")

   def getLastTrame(self):
      return self.lastTrame
      
   # fonction de mise en base de données
   def insertBdd(self):
      trameLoop2 = self.getTrameStr()
      try:
         with self.connection.cursor() as cursor:
            sql = "INSERT INTO trame (date_heure, trame) VALUES (NOW(), '" + str(trameLoop2) + "');"
            
            cursor.execute(sql)
            self.connection.commit()
            trame_id = cursor.lastrowid
            
            sql="INSERT INTO `releve` (`trame_id`, `barometer`, `inside_temperature`, `inside_humidity`, `outside_temperature`, `wind_speed`, `wind_direction`) VALUES ("+str(trame_id)+", "+str(self.barometer)+", "+str(self.inside_temperature)+", "+str(self.inside_humidity)+", "+str(self.outside_temperature)+", "+str(self.wind_speed)+", "+str(self.wind_direction)+");"
            cursor.execute(sql)
            self.connection.commit()
            
      except ValueError:
         print("Impossible d'enregistrer la trame");
         
   # fonction de décodage de la trame
   def decodeTrame(self):
   
      ### barometer | Offset : 7 | Size : 2
      self.barometer = self.lastTrame[8] * 256 + self.lastTrame[7]
      
      #barometer_mbar = 33.86 * (self.barometer / 1000)
      #print(str(barometer_mbar) + "mbar")

      ### inside_temperature | Offset : 9 | Size : 2
      self.inside_temperature = self.lastTrame[10] * 256 + self.lastTrame[9]

      #insideTemperatureFarenheit = self.inside_temperature / 10
      #insideTemperature = (insideTemperatureFarenheit - 32) / 1.8
      #print("Température intérieure : " + str(insideTemperature) + "°C")

      ### inside_humidity | Offset : 11 | Size : 1
      self.inside_humidity = self.lastTrame[11];

      ### outside_temperature | Offset : 12 | Size : 2
      self.outside_temperature = self.lastTrame[13] * 256 + self.lastTrame[12];

      #outsideTemperature = ((self.outside_temperature / 10) - 32) / 1.8;

      ### wind_speed | Offset : 14 | Size : 1
      self.wind_speed = self.lastTrame[14];

      ### wind_direction | Offset : 16 | Size : 2
      self.wind_direction = self.lastTrame[17] * 256 + self.lastTrame[16];
      
   def byte_afficherBytearrayHexa(self, tableOctet, separateur = ' '):
      """ Affiche le contenu d'un type bytearray (tableau d'octets) en hexadécimal
         Chaque octet est séparé par le séparateur passé en paramètre : '', ' ', '/' ...
         Exemple 1 : 
            paramètre entrée -> (bytearray[0x10, 0x00, 0xFE, 0x13, 0x4A], ' ')
            affichage -> 10 00 fe 13 4a
         Exemple 2 : bytearray contenant les codes ascii du message textuel "Hello world!"
            paramètre entrée ->  
              (bytearray[0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64, 0x21], ' ') 
            affichage -> 48 65 6c 6c 6f 20 77 6f 72 6c 64 21
      """
      for idx, octet in enumerate(tableOctet):
         if idx != len(tableOctet) - 1:
            print("%s%s" % ('{:02x}'.format(octet), separateur), end ='')
         else:    # évite d'afficher le séparateur après le dernier octet affiché
            print('{:02x}'.format(octet))   
   
   def getTrameStr(self):
      trame = ""
      for idx, octet in enumerate(self.lastTrame):
         if idx != len(self.lastTrame) - 1:
            trame += ("%s%s" % ('{:02x}'.format(octet), ''))
         else:    # évite d'afficher le séparateur après le dernier octet affiché
            trame += ('{:02x}'.format(octet))   
      return trame
   