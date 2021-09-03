# 
# File: intro-ex-44.py
# Auth: Martin Burolla
# Date: 9/3/2021
# Desc: HL7 Old School
#

def reverseName(name):
  retval = ""
  array = name.split('^')
  retval = f"{array[1]} {array[0]}"
  return retval

def parsePIDSegments(filename):
  retval = []
  f = open(filename, "r")
  lines = f.readlines()
  for l in lines:
    if l[0:3] == 'PID':
      retval.append(l)
  f.close()
  return retval

def main():
  patientDict = {
    '111-11-1111' : 'John Smith', 
    '222-22-2222' : 'Sue Anderson',
    '333-33-3333' : 'Tim McCoy'
  }

  pidSegmentList = parsePIDSegments("oru-r01.hl7")

  # Build name tuple list from PID Segments.
  nameTupleList = []
  for pid in pidSegmentList:
    array = pid.split('|')
    ssn = array[19]
    name = reverseName(array[5])
    nameTupleList.append((ssn, name)) # A list of tuples.
   
  # Check the names against our list and the patientDict.
  for nameTuple in nameTupleList:
    if patientDict[nameTuple[0]].lower() == nameTuple[1].lower():
      print(f'{nameTuple[0]} {nameTuple[1]}: OK')
    else:
      print(f'{nameTuple[0]} {nameTuple[1]}: No Match!!!')

if __name__ == "__main__":  
  main()
