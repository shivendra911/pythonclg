Variables
--> Python is a "dynamically typed".
means we dont need to define type of variabe first.
-> a variable is a refecence/label in memory address.
e.g. x = 5
     y = x
     x = 'new data'
     y = "Computer"

Naming python variables
->we cant start from numbers and special symbols and use special symbols anywhere but can use underscore(_).

Assigning multiple values 
eg. a,b,c = 1,2,3

Memory mapping
id()


Constants in Python

Python does not have true constants like const in C/C++.
By convention, constants are variables written in uppercase and are treated as read-only by programmers.

1. Using constants by convention (recommended)
PI = 3.14159
MAX_USERS = 100
APP_NAME = "MyApp"


Uppercase names indicate constants

Python does not prevent modification, but it signals “do not change”

PI = 3.14   # Allowed, but bad practice

2. Constants inside a separate module (best practice)

Create a file constants.py:

PI = 3.14159
GRAVITY = 9.8
MAX_RETRIES = 5


Use it in another file:

import constants

print(constants.PI)
print(constants.GRAVITY)


This approach avoids accidental reassignment.

3. Using typing.Final (Python 3.8+)

This helps static type checkers (like mypy), but not enforced at runtime.

from typing import Final

PI: Final = 3.14159
MAX_USERS: Final = 100


Reassigning will raise a warning in type checkers:

PI = 3.14   # Warning (not runtime error)

4. Using enum.Enum for fixed values

Useful when values represent choices.

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


Usage:

print(Color.RED)

5. Using dataclass with frozen=True

Creates immutable objects.

from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    HOST: str = "localhost"
    PORT: int = 8080


Attempting to modify raises an error.

What NOT to do
const PI = 3.14   # SyntaxError


Python has no const keyword.

Python does not support true constants; constants are defined using uppercase variable names by convention.





Taking inputs
input()

num = int(input())


Operators

1. Arithmetic operators
+ Addition
- Subtraction
* Multiplication
/ Division
// Floor Division
% modulus
** power

