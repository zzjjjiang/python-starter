#
# File: app.py
# Auth: Martin Burolla
# Date: 8/9/2021
# Desc: Data access
#

import boto3
import pymysql
from AuroraDBProxy import AuroraDBProxy

def main():
  # with AuroraDBProxy() as auroraDBProxy:
  #   data = auroraDBProxy.getAllPeople()
  # print(data)

  USER = 'sia-db-user'
  HOST = 'sia-db-cluster-instance-1.cosgu9wr5iwp.us-east-1.rds.amazonaws.com'
  PWD = 'testtest'
  DB = 'sia-db'

  client = boto3.client('rds')
  
  connection = pymysql.connect(
    auth_plugin_map = {'mysql_cleartext_password': None},
    user = USER,
    host = HOST,
    password = PWD,
    database = DB)

  with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    cursor.execute('select * from person')
  connection.commit()
  people = cursor.fetchall()
  print(people)

  
if __name__ == "__main__":  
  main()
