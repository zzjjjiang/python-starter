#
# File: test_ex-1.py
# Auth: Martin Burolla
# Date: 9/5/2021
# Desc:
#

import businessLogicModule

#
# Test Methods
#

def test_Add_Numbers_Function():              
  # Arrange
  x = 1
  y = 2

  # Act 
  r = businessLogicModule.addNumbers(1,2)

  # Assert
  assert r == 3, "add() function failed"

def test_Concat_Strings_Function():              
  # Arrange
  x = "Hello"
  y = "World"

  # Act 
  r = businessLogicModule.concatStrings(x, y)

  # Assert
  assert "Hello" in r, "Hello not in Hello World"
  assert "World" in r, "World not in Hello World"

#
# Helper methods
#

def foo():
  print('herererere *************************************')
