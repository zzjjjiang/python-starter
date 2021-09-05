#
# File: test_ex-1.py
# Auth: Martin Burolla
# Date: 9/5/2021
# Desc:
#

import sia
import pytest

dbConn = None

#
# Fixture
#

# @pytest.fixture
# def dbConn():
#   dbConn = "Connected"
#   return dbConn

#
# Setup/Tear Down
#

def setup_module(module):
  global dbConn
  # Create test user data...
  dbConn = "Connected"

def teardown_module(module):
  global dbConn
   # delete test user data...
  dbConn = None

#
# Test Methods
#

def test_DoubleList():
  # Arrange
  l = [1,2,3,4]

  # Act
  doubleList = sia.doubleList(l)

  # Assert  
  assert doubleList[0] == 2, "Value 1 expected to be 2"
  assert doubleList[1] == 4, "Value 2 expected to be 4"
  assert doubleList[2] == 6, "Value 3 expected to be  6"
  assert doubleList[3] == 8, "Value4 expected to be 8"
    
def test_DoubleList_String():
  # Arrange
  l = ["test"]

  # Act
  doubleList = sia.doubleList(l)

  # Assert  
  assert doubleList[0] == "testtest"


def test_Add_Numbers_Function():              
  # Arrange
  x = 1
  y = 2

  # Act 
  r = sia.addNumbers(1,2)

  # Assert
  assert dbConn == "Connected"
  assert r == 3, "add() function failed"

  # Clean up (Nothing to cleanup)

def test_Concat_Strings_Function():             
  # Arrange
  x = "Hello"
  y = "World"

  # Act 
  r = sia.concatStrings(x, y)

  # Assert
  assert dbConn == "Connected"
  assert "Hello" in r, "Hello not in Hello World"
  assert "World" in r, "World not in Hello World"

  # Clean up (Nothing to cleanup)

#
# Helper methods
#

def foo():
  print('I am a helper method because I do not start with test.')
