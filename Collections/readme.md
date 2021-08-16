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

# Template
```
def your_function_here():
  # TODO
  pass

def main():
  your_function_here()

if __name__ == "__main__":  
    main()
```

# Ex 1: Every Other Color
- Create a program that contains a function that accepts a List of colors and returns every other one and prints the results.

# Ex 2: Remove Dupes
- Create a program that contains a function that takes two Lists of numbers and returns one List without any duplicates with the numbers in descending order.

Input:
```
  list1 = [7,6,5,4,3,2,1]
  list2 = [10,9,8,7,6,5,4,3]
```
Ouput:
```
  [10,9,8,7,6,5,4,3,2,1]
```

# Ex 3: Sum of Ages
- Create a program that contains a function that returns the sum of a List of people passed into it:
 ```
    name: Peter, age: 20
    name: Paul,  age: 30
    name: Mary,  age: 40
```
HINT: The PeopleList is a List of JSON objects.

# Ex 4: Car Models
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

# Ex 5: Find Longest List
-  Create a program that contains a function that accepts three Lists and returns the length of the longest one.

# Ex 6: Create, Sum and Sammy
- Create a program that contains two functions: 
```
createList
sumList
```
The createList function creates the following List of numbers: [1,2,3,4,5,6,7,8,9,10].
The sumList function accepts a List and sums the values in the List (Sum: 55).
The program must use an f-string to print sum of all the values in the List:
```
"I can't drive 55."
```
# Ex 7: Length of Words
- Create a program that contains a function that accepts a sentence and returns a List that contains the length of each word.

Example: `The quick brown fox jumps over the lazy dog`
Output:`[3, 5, 5, 3, 5, 4, 3, 4, 3]`

# Ex 8: Peter's Ford
- Create a program that contains the following dictionary:
  ```
  carDictionary = {
     'peter': { 'brand' : 'Ford', 'model' : 'Mustang' },
     'paul': { 'brand' : 'Toyota', 'model' : 'Prius' },
     'mary': { 'brand' : 'Chevy', 'model' : 'Corvette' },
   }
  ```
  The program must use an f-string to query the dictionary for peter's car and prints the following output:

  `Peter drives a Ford Mustang.`

# Ex 9: Joe's Tuple
- Create a program that contains a function that accepts three arguments and returns a Tuple:
```
age
firstname
state
```
The program prints the Tuple to the console:

Example: `(40, 'Joe', 'New York')`

# Ex 10: Parts is Parts
- Create a program that contains the following dictionary:

```
  partsDictionary = {
    "Screw" : [ { "inStock": True }, { "color" : "silver" }, { "partNumber" : "123" }, { "cost" : 1.00 } ],
    "Hammer" : [ { "inStock": True }, { "color" : "silver" }, { "cost" : 10.00 } ],
    "Bolt" : [ { "inStock": True }, { "color" : "silver" }, { "cost" : 1.00 } ],
    "Nail" : [ { "inStock": False }, { "color" : "silver" }, { "cost" : .10 } ],
    "Wood" : [ { "inStock": True }, { "cost" : 3.00 } ],
  }

```
The program sums the cost for all the parts that are in stock and writes the following to the console:

```
Total Cost: $15.00.
```






# Final?
- Create a program that contains a Dictionary of 10 people that stores the following data:
  - First Name 
  - Last Name
  - Salary
The key for this dictionary is the user's social security number.  The program also contains a List of social security numbers matching that stored in the Dictionary.  The program loops though the List and obtains information for this person from the people dictionary.  The output of the program prints the salary for all the people in the List.






