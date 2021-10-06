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

def getPerson(personId):
  retval = []
  conn = createConnection()
  with conn.cursor(pymysql.cursors.DictCursor) as cursor:
    cursor.execute('select * from person where id = %s', (personId)) # personId is substituted for %s.
    conn.commit()
  retval = cursor.fetchone()
  return retval

def getPeople():
  retval = []
  conn = createConnection()
  with conn.cursor(pymysql.cursors.DictCursor) as cursor:
    cursor.execute('select * from person')
    conn.commit()
  retval = cursor.fetchall()
  return retval

def insertPerson(personName):
  retval = 0
  conn = createConnection()
  with conn.cursor() as cursor:
    cursor.execute("insert into person (name) values (%s)", (personName)) # personName is substituted for %s.
    retval = cursor.lastrowid
    conn.commit()
  return retval

def updatePerson(id, name): # Note the order of id and name here doesn't matter.
  conn = createConnection()
  with conn.cursor() as cursor:
    cursor.execute("update person set name = %s where id = %s;", (name, id)) # name, and id is substituted name and id, the order of name and id matters here.
    conn.commit()

def insertDemo(firstName, lastName):
  retval = 0
  conn = createConnection()
  with conn.cursor() as cursor:
    cursor.execute("insert into demo (firstname, lastname) values (%s, %s)", (firstName, lastName))
    retval = cursor.lastrowid
    conn.commit()
  return retval

def main():
  # INSERT
  # id = insertDemo('joe', 'green')
  # print(id)

  # id = insertPerson('Billy')
  # print(f"Person Id: {id}.")

  # SELECT
  # people = getPeople()
  # print(people)

  # UPDATE
  updatePerson(1, 'Joey Jr.') # Do the update
  person = getPerson(1) # Did the update work?
  print(person)
  pass

if __name__ == "__main__":  
  main()
