#
# File: Person.py
# Auth: Martin Burolla
# Date: 8/8/2021
# Desc: Represents a person in our business domain.

from datetime import date


class Person: 
    
    #
    # Constructors
    #

    def __init__(self, name, age): 
        self.name = name
        self.age = age
        self.ssn = ''
        self.__lookUpSSN()
      
    @classmethod  # Constructor overloading
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year)
      
    #
    # Public methods
    #

    def speak(self):
        return f"My name is {self.name} and I am {self.age} years old."

    @staticmethod
    def isAdult(age): 
        return age > 18

    #
    # Private methods
    #

    def __lookUpSSN(self):
        self.ssn = 'xxx-xxx-xxxx'

    #
    # Dunder
    #

    def __len__(self):
        return len(self.name)

    def __repr__(self):
        return f'Person: {self.name, str(self.age)}'
