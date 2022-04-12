#
# File: AuroraDBProxy.py
# Auth: Martin Burolla
# Date: 5/6/2021
# Desc: Wrapper for AWS Aurora DB that returns Python dictionaries.
#

import boto3
import pymysql
import configparser

class AuroraDBProxy(object): 

    #
    # SQL Statements
    #
    
    ## Reads

    SELECT_PERSON = 'select * from person;'

    #
    # Constructors
    #
    
    def __init__(self): 
      self.connection = None
      config = configparser.ConfigParser()
      config.read('./config.ini')
      self.__getDatabaseConfig()
      
    #
    # Public Methods
    #

    def getAllPeople(self):
      retval = None
      with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(self.SELECT_PERSON) # (requestId))
      self.connection.commit()
      retval = cursor.fetchall()
      return retval

    # 
    # Private Methods
    #

    def __getDatabaseConfig(self):
      config = configparser.ConfigParser()
      config.read('./config.ini')
      self.DB = config['Database']['DB']
      self.PORT = config['Database']['PORT']
      self.HOST = config['Database']['HOST']
      self.USER = config['Database']['USER']
      self.REGION = config['Database']['REGION']

    def __createConnection(self):
      client = boto3.client('rds')
      token = client.generate_db_auth_token(DBHostname = self.HOST, Port = self.PORT, DBUsername = self.USER, Region = self.REGION)
      self.connection = pymysql.connect(
        auth_plugin_map = {'mysql_cleartext_password': None},
        user = self.USER,
        host = self.HOST,
        password = token,
        database = self.DB,
        ssl = {'ca': './rds-combined-ca-bundle.pem'})

    def __closeConnection(self):
      self.connection.close()

    #
    # Dunder
    #

    def __enter__(self):
      self.__createConnection()
      return self

    def __exit__(self, exc_type, exc_val, exc_tb):
      self.__closeConnection()
