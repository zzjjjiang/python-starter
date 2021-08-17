# Intro
Beginner assignments.

# Ex 1: Random number
Create a program that creates a list of 10 random numbers and sums all the numbers.  The result is printed to the console.  The numbers in the list range from 0 - 100.  The program must use an f-string to display the output.

Example list: [1,34,2,33,45,67,24,87,32,38]

Example Output:
```
The sum is: <random number>
```

# Ex 2: Python in a Box
Create a program that uses the `input()` function to obtain the width, height and length of a box.  The program computes the volume of the box (width * height * length) and writes it to the console:

Example input:
```
Enter width: 1.1 
Enter height: 1.2
Enter length: 1.3
```

Example output:
```
Volume is: 1.72.
```

# Ex 3: First and Last
Create a program that accepts a list of numbers using the `input()` function and writes `True` if the first and last numbers are the same, otherwise write `False` to the console.

Example input:
```
Enter list of numbers: 1,2,3
```

Example output:
```
False
```
# Ex 4: Word Count
Create a program that counts the number of times the word `Python` appears in the text below and writes the result to the console. Do not use the `string.count()` method.

```
"Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
```
 Example output:
```
3
```

# Ex 5: Bigger Set
Create a program that adds the following List of numbers to the Set and writes the final Set to the console:
```
myList = [1,2,3]
mySet = {3,4,5}
```
Example output:
```
{1,2,3,4,5}
```
# Ex 6: Reverse Me
Create a program that writes the following list of numbers in reverse order to the console:
```
[11, 100, 101, 999, 1001]
```
Example output:
```
[1001, 999, 101, 100, 11]
```

# Ex 7: Winner Winner
Create a program that generates a randon number between 1 and 100.  If the number is less than 10 the program prints the value of the number and `You lose.` on the console.  If the number is greater than 10 and less than 50 the program prints the value of the number and `Try again.` on the console.  If the number is greater than 50 the program prints the value of the number and `You win!` on the console.

Example output:
```
9: You lose.
17: Try again.
86: You win!
```

# Ex 8: Shortest Straw
Create a program that finds the smallest number in this list and writes the result to the console.  Do not use the `min()` function.
```
myList = [6,2,7,3,77,7,1]
```

# Ex 9: Uppers or Lowers
Create a program that writes `True` to the console if a string is upper case, `False` if a string is not.

Example input:
```
Enter string: "HELLO"
```

Example output:
```
True
```

# Ex 10: Vs and Cs
Create a program that counts all the vowels and consonants in a string and writes the count to the console:

Example input:
```
Enter string: Apple
```
```
Example output:
Vowels: 2
Consonants: 3
```

# Ex 11: Write Date Today
Create a program that writes the current date to a file named: `output.txt`.  The program must use an f-string when writing to a file.

File Contents:
```
Today's date is: 08/17/2021.
```

# Ex 12: Negative to Positive / Positive to Negative
Create a program that prompts the user to enter an integer value.  The program converts a positive integer to a negative integer, and converts a negative integer to a positive integer.  The result is written to the console. The program returns an error is a float (decimal) is entered.

Examples:
```
Enter integer: 12
-12
```

```
Enter integer: -133
133
```

```
Enter integer: 123232.1
ERROR: 123232.1 is not an integer.
```