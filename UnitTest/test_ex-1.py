#
# File: test_ex-1.py
# Auth: Martin Burolla
# Date: 9/5/2021
# Desc:
#

import pytest
import businessLogicModule

dbConn = None

#
# Fixture
#

@pytest.fixture
def dbConn():
  dbConn = "Connected"
  return dbConn

#
# Setup/Tear Down
#

def setup_module(module):
  global dbConn
  dbConn = "Connected"

def teardown_module(module):
  global dbConn
  dbConn = None

#
# Test Methods
#

def test_Add_Numbers_Function(dbConn):              
  # Arrange
  x = 1
  y = 2

  # Act 
  r = businessLogicModule.addNumbers(1,2)

  # Assert
  assert dbConn == "Connected"
  assert r == 3, "add() function failed"

  # Clean up (Nothing to cleanup)

def test_Concat_Strings_Function():              
  # Arrange
  x = "Hello"
  y = "World"

  # Act 
  r = businessLogicModule.concatStrings(x, y)

  # Assert
  assert dbConn == "Connected"
  assert "Hello" in r, "Hello not in Hello World"
  assert "World" in r, "World not in Hello World"

  # Clean up (Nothing to cleanup)

#
# Helper methods
#

def foo():
  print('herererere *************************************')
