#what is module in python?
# A module in Python is a file that contains Python code, which can define functions, classes, and variables. 
# It allows for code organization and reuse across different programs.
#  Modules can be imported into other Python files using the import statement.
# Example of a simple module (module.py):
def info(**data):
    return data

def total(*nums):
    return sum(nums)

def add(a, b):
    return a + b   

def subtract(a, b):
    return a - b    

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
    
def square(a):
    return a * a

def cube(a):
    return a * a * a
