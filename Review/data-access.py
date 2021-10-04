#
# File: app.py
# Auth: Martin Burolla
# Date: 10/4/2021
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
  conn = createConnection()
  # Querying...
  with conn.cursor(pymysql.cursors.DictCursor) as cursor:
    cursor.execute('select * from person')
  conn.commit()
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

def updatePerson(id, name):
  conn = createConnection()
  with conn.cursor() as cursor:
    cursor.execute("update person set name = %s where id = %s;", (name, id))
  conn.commit()

def main():
  # INSERT
  id = insertPerson('Billy')
  print(f"Person Id: {id}.")

  # SELECT
  # people = getPeople()
  # print(people)

  # UPDATE
  # updatePerson(1, 'Joey Jo Jo')
  # print(id)

if __name__ == "__main__":  
  main()
