# Python Starter 
Assignment repo that illustrates the core concepts found in the Python programming language. Assignments are located [here](./assignments.md)

# Videos
[Python for Beginners - Learn Python (1h)](https://youtu.be/kqtD5dpn9C8)

# Links
[Python docs](https://docs.python.org/3.10/)

# Contents
- [Classes](./Classes)
- [Data Access](./DataAccess)
- [Collections](./Collections)
- [Exceptions](./Exceptions)
- [Functions](./Functions)
- [AWS-SDK](./AWS-SDK)
- [Unit Testing](./UnitTest)
- [Git](./Git)

# Quick Reference Guides
- [Data Structures (Collections)](./Reference-Guides/collections-rg.py)
- [Database (DDL/DML)](./Reference-Guides/database-rg.sql)
- [Functions-1](./Reference-Guides/functions1-rg.py)
- [Functions-2](./Reference-Guides/functions2-rg.py)
- [Lambda Filter Map](./Reference-Guides/lambda-filter-map-rg.py)
- [List Comprehension](./Reference-Guides/list-comprehension-rg.py)
- [Truthy Falsey](./Reference-Guides/truthy-falsey-rg.py)

# Python
Python is a dynamic, interpreted (bytecode-compiled) language. There are no type declarations of variables, parameters, functions, or methods in source code. This makes the code short and flexible, and you lose the compile-time type checking of the source code. Python tracks the types of all values at runtime and flags code that does not make sense as it runs.

Python does very little checking at compile time, deferring almost all type, name, etc. checks on each line until that line runs. Suppose the above main() calls repeat() like this:

```
def main():
    if name == 'Guiseppe':
        print repeeeet(name) + '!!!'
    else:
        print repeat(name)
```

The if-statement contains an obvious error, where the repeat() function is accidentally typed in as repeeeet(). The funny thing in Python ... this code compiles and runs fine so long as the name at runtime is not 'Guido'. Only when a run actually tries to execute the repeeeet() will it notice that there is no such function and raise an error. This just means that when you first run a Python program, some of the first errors you see will be simple typos like this. This is one area where languages with a more verbose type system, like Java, have an advantage ... they can catch such errors at compile time (but of course you have to maintain all that type information ... it's a tradeoff).
