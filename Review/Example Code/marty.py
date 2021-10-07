#
# File: app.py
# Auth: Martin Burolla
# Date: 10/4/2021
# Desc: Data access
#

from time import sleep
from datetime import datetime
import pymysql # <== need to install dependencies: pip install pymysql

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
    cursor.execute('select * from person where id = %s;', (personId)) # personId is substituted for %s.
    conn.commit()
    retval = cursor.fetchone() # <== Return only ONE result.
  return retval

def getPeople():
  retval = []
  conn = createConnection()
  with conn.cursor(pymysql.cursors.DictCursor) as cursor:
    cursor.execute('select * from person;')
    conn.commit()
    retval = cursor.fetchall() #<== Return all rows from the query.
  return retval

def insertPerson(personName):
  retval = 0
  conn = createConnection()
  with conn.cursor() as cursor:
    cursor.execute("insert into person (name) values (%s);", (personName)) # personName is substituted for %s.
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
  with conn.cursor() as cursor: # "with" means we are using Python's context manager, so we don't have to close things.
    cursor.execute("insert into demo (firstname, lastname) values (%s, %s);", (firstName, lastName))
    retval = cursor.lastrowid # Get the ID of the row we just inserted.
    conn.commit() # Force the DB accept our change.
  return retval # Return the ID we just inserted.

def insertMarty(guitarName, carName, computerName):
  retval = 0
  conn = createConnection()
  with conn.cursor() as cursor: 
    cursor.execute("insert into marty (guitar_name, car_name, computer_name) values (%s, %s, %s);", (guitarName, carName, computerName))
    retval = cursor.lastrowid 
    conn.commit() 
  return retval 

def getMarty():
  retval = []
  conn = createConnection()
  with conn.cursor(pymysql.cursors.DictCursor) as cursor:
    cursor.execute('select * from marty;')
    conn.commit()
    retval = cursor.fetchall()
  return retval

def getPatients(bankName):
  retval = []
  sql = '''
    select 
      p.name
    from 
      patient p 
      join patient_bank pb on p.patient_id = pb.patient_id
      join bank b on b.bank_id = pb.bank_id
    where 
      b.name = %s;
  '''
  conn = createConnection()
  with conn.cursor(pymysql.cursors.DictCursor) as cursor:
    cursor.execute(sql, (bankName))
    conn.commit()
    retval = cursor.fetchall()
  return retval

def main():
  # INSERT
  # id = insertMarty('Carvin', 'Toyota', 'Linux')
  # print(id)

  # id = insertPerson('Billy')
  # print(f"Person Id: {id}.")

  # martyRows = getMarty()
  # print(martyRows)

  # bofaList = getPatients(bankName = 'Bank of America') # Named parameter.
  # print(bofaList)

  
  # age = 11
  # if age <=10:
  #   print('young')
  # elif age > 10 and age <= 20:
  #   print('medium')
  # elif age > 20:
  #   print('old')

  


  # # SELECT
  # while True:
  #   timestamp = datetime.today().strftime('%m/%d/%Y %I:%M:%S %p')
  #   pl = getPeople()
  #   print(pl)
  #   if len(pl) >= 5:
  #     print('ALERT!!!!!!!! TABLE IS TOO LARGE!!!')
  #   print(f'*** Last run: {timestamp}. ***')
  #   sleep(5)


  
  #l1 = list(filter(lambda p : p['name'] == 'Batman', peopleList))
  #l2 = list(map(lambda x : x['name'], peopleList))
  #print(l2)

  # UPDATE
  # updatePerson(1, 'Joey Jr.') # Do the update
  # person = getPerson(1) # Did the update work?
  # print(person)
  pass

if __name__ == "__main__":  
  main()
