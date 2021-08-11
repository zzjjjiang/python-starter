# Collections

# Notes
- Tuples
 - Are immutable
- Lists
 - General use
- Dictionaries
 - Keys are immutable
 - FAST lookups
- Sets 
 - Only support unique values
 - Venn diagram

# Ex 1
- Create a program that contains a function that accepts a List of colors and returns every other one and prints the results.

# Ex 2
- Create a program that contains a function takes two Lists of numbers and returns one List without any duplicates with the numbers in descending order.

# Ex 3
- Create a program that contains a function that returns the sum of a List of people passed into it:
 ```
    name: Peter, age: 20
    name: Paul,  age: 30
    name: Mary,  age: 40
```
HINT: The PeopleList is a list of JSON objects.

# Ex 4
- Pre-req: http://jsonviewer.stack.hu/
- Create a program that contains a function that accepts a Dictionary and a List.  The dictionary is the following:
  ```
  carDictionary = {
     'peter': { 'brand' : 'Ford', 'model' : 'Mustang' },
     'paul': { 'brand' : 'Toyota', 'model' : 'Prius' },
     'mary': { 'brand' : 'Chevy', 'model' : 'Corvette' },
   }
  ```
  The List is the following:

  ```
  peopleList = ['peter', 'mary']
  ```

  The function returns a String that contains the models of cars that peter and mary own ("Mustang, Corvette")

# Bigger
- Create a program that contains a Dictionary of 10 people that stores the following data:
  - First Name 
  - Last Name
  - Salary
The key for this dictionary is the user's social security number.  The program also contains a List of social security numbers matching that stored in the Dictionary.  The program loops though the List and obtains information for this person from the people dictionary.  The output of the program prints the salary for all the people in the List.






