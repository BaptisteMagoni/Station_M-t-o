# -*- coding: utf-8 -*-
try:
  import mysql.connector
except:
  print("Module mysql pas trouvé")

class SqlConnection:

  def __init__(self, m_host, m_user, m_password, m_database):
    self.host = m_host
    self.user = m_user
    self.password = m_password
    self.database = m_database
  
  def connexion(self):
    try:
      self.conn = mysql.connector.connect(host=self.host,user=self.user,password=self.password, database=self.database)
      self.cursor = self.conn.cursor()
    except:
      print("Problème de connexion à la base de donnée")
  
  def insert_data(self, data):
    if type(data) is tuple:
      try:
        self.connexion()
        self.cursor.execute("""INSERT INTO measure (Trame, Packet_Type, Bar_Trend, Barometer, Inside_Temperature, Inside_Humidity, Outside_Temperature, Wind_speed, Wind_direction) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", data)
        self.conn.commit()
        print("Insert ok !")
      except ValueError as err:
        print("Probl�me dans le insert : {}".format(err))
    else:
      print("La variable n'est pas de type tuple")