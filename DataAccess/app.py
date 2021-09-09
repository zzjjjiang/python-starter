#
# File: app.py
# Auth: Martin Burolla
# Date: 8/9/2021
# Desc: Data access
#

import pymysql

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


def main():
  people = getPeople()
  print(people)

if __name__ == "__main__":  
  main()

