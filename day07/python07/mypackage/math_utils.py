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
    
def power(a, b):
    return a ** b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a    


def lcm(a, b):
    return abs(a * b) // gcd(a, b)      


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 