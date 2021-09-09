#
# File: app.py
# Auth: Martin Burolla
# Date: 8/9/2021
# Desc: Data access
#

import pymysql

def createConnection():
  retval = None  
  USER = 'sia-db-user'
  HOST = 'sia-db-cluster-instance-1.cosgu9wr5iwp.us-east-1.rds.amazonaws.com'
  PWD = 'testtest'
  DB = 'sia-db'

  retval = pymysql.connect(
    user = USER,
    host = HOST,
    password = PWD,
    database = DB)
  return retval

def getPeople():
  retval = []

  # Connecting...
  USER = 'sia-db-user'
  HOST = 'sia-db-cluster-instance-1.cosgu9wr5iwp.us-east-1.rds.amazonaws.com'
  PWD = 'testtest'
  DB = 'sia-db'

  connection = pymysql.connect(
    user = USER,
    host = HOST,
    password = PWD,
    database = DB)

  # Querying...
  with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    cursor.execute('select * from person')
  connection.commit()
  retval = cursor.fetchall()
  return retval

def insertPerson(personName):
  retval = 0
  conn = createConnection()
  with conn.cursor() as cursor:
    cursor.execute("insert into person (name) values (%s)", (personName))
    retval = cursor.lastrowid
  conn.commit()
  return retval

def main():
  id = insertPerson('Tom')
  print(f"Person Id: {id}.")
  people = getPeople()
  print(people)

if __name__ == "__main__":  
  main()

