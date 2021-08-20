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
Create a program that finds the smallest number in this list and writes the result to the console.  Do not use the `min()` or `sort()` functions.
```
myList = [6,2,7,3,77,7,1]
```
Example output:
```
1
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
Create a program that counts all the vowels and consonants in a word and writes the count to the console:

Example input:
```
Enter string: Apple
```

Example output:
```
Vowels: 2
Consonants: 3
```

# Ex 11: Write Today's Date
Create a program that writes the current date to a file named: `output.txt`.  The program must use an f-string when writing to a file.

File Contents:
```
Today's date is: 08/17/2021.
```

# Ex 12: Negative to Positive / Positive to Negative
Create a program that prompts the user to enter an integer value.  The program converts a positive integer to a negative integer, and converts a negative integer to a positive integer.  The result is written to the console. The program returns an error if the user enters a float value.  Do not use the `abs()` function.

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

# Ex: 13 Add Only Calculator
Create a program that prompts the user for two integers and adds them.  The program runs indefinitely until `exit` is typed.

Example:
```
Enter first integer: 1
Enter second integer: 3
Answer: 4.
Enter first integer: 5
Enter second integer: 5
Answer: 10.
Enter first integer: exit
```

# Ex: 14 Forever Calculator
Extend Exercise 13 and create a program that prompts the user for two integers.  The program also asks the user for a mathmetical operation (add, subtract, multiply, divide).  The program runs indefinitely until `exit` is typed.  Ensure the program does not crash when dividing by zero.

Example usage:
```
Enter first integer: 3
Enter second integer: 1
Enter operation (add, sub, mul, div): sub
Answer: 2.0
Enter first integer: 3
Enter second integer: 4
Enter operation (add, sub, mul, div): mul
Answer: 12.0
Enter first integer: exit
```

# Ex: 15 Forever Calculator Logger
Extend Exercise 14 and log every calculation to a file named `output.txt`.

Example log file:
```
08/17/2021 07:59:36 PM: 1.0 add 2.0 = 3.0
08/17/2021 07:59:40 PM: 4.0 sub 5.0 = -1.0
08/17/2021 07:59:44 PM: 2.0 mul 6.0 = 12.0
08/17/2021 07:59:51 PM: 1.0 div 2.0 = 0.5
```

# Ex: 16 Hash It, Print It
Hashing is often applied to passwords.  Instead of storing raw passwords in backend systems, passwords are hashed (optionally with a salt value) and the hash value is stored.

Create a program that prompts the user to enter a username and password.  The program hashes the password
using the `sha256()` algorithm and stores it in a dictionary.  The key for the dictionary is the user name.  The program loops forever unti `exit` is entered.  When `exit` is entered the program prints the key/value pairs from the dictionary to the console.

Example Usage:
```
Enter username: mburolla
Enter password: test
Enter username: joe
Enter password: test2
Enter username: exit
mburolla : 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
joe : 60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752
```

# Ex: 17 Simple Authentication, No Authorization
#### Background
Authentication is the process in which a set of credentials is validated.  Authorization is what the user is allowed to do once they have been Authenticated. To summarize, Authentication is proving who you are and Authorization is what you are allowed to do.

Extend the program created in Exercise 16 and prompt the user to select one of two modes: 
#### Add User 
"Add user mode" adds users to the dictionary (essentially Exercise 16).
#### Login 
"Login mode" provides a user to login with their username and password.  The program prints `Password is correct.` when the user has entered the correct password, and prints `Incorrect password.` when the password is incorrect.  If the user does not exist in the dictionary, print `User does not exist.`.

Example Usage:

```
Type exit at anytime to end program...
Enter mode (add|login): add
Enter username: mburolla
Enter password: test
Enter mode (add|login): login
Enter username: mburolla
Enter password: test
Password is correct.
Enter mode (add|login): login
Enter username: mburolla
Enter password: wrongpassword
Incorrect password.
Enter mode (add|login): exit
mburolla : 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
```

#### Pseudocode
```
main: 
  
  dictonary = {}

  loop:
    mode = input(enter mode)

    if mode is add:
      ex 16 stuff here...

    if mode is login:
      New stuff here...
      username = input(username)
      password = input(password)

      hashpassword = hash(password)
      lookup hashpassword for this user in dictionary
      compare hashes, print results
```

# Ex: 18 Random Number Game
Create a program generates a random number 1-10 inclusive.  Th program prompts the user to enter a number between 1-10.  If the user number is too low the program prints (`Too low`).  If the user number is too high, the program prints (`Too high`).  If the user number is equal to the number the program generated print (`You guessed it!!!`) and the program terminates.

Example Usage:
```
Enter a number between 1-10: 5
Too high
Enter a number between 1-10: 1
Too low
Enter a number between 1-10: 4
Too high
Enter a number between 1-10: 3
Too high
Enter a number between 1-10: 2
You guessed it!!!!
```

# Ex: 19 Frame It
Create a program that contains a list of strings and prints them in a frame on the console:

```
wordlist = ["Hello", "World", "in", "a", "frame"]
```
```
*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
```

# Ex: 20 Super Simple File Indexer
Create a program that reads the words from the following file: [input-file-1.txt](http://www.google.com).  The program contains a dictionary that keeps track of the word count and prints the results to the console.

Example output:
```
This:4
is:4
a:1
test:1
to:1
see:1
how:1
.
.
.
``