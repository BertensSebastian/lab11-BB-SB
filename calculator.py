"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
<<<<<<< HEAD
# First example
import math
def add(a, b): 
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def log(a, b):
    if a<=0 or b<=0:
        raise ValueError
    return math.log(base=a,x=b)

def exp(a, b):
    return a**b


=======
import math


def add(a, b): 
    return a + b

def subtract(a ,b):
    return a-b

def multiply(a ,b):
    return a*b

def divide(a ,b):
    if a ==0:
        return ZeroDivisionError
    else:
        return b/a

def logarithm(a ,b):
    if a<=0:
        return ValueError
    elif b<=0:
        return ValueError
    else:
        return math.log(b, a)

def exponent(a ,b):
    return a**b
>>>>>>> 78d2029ba71b36198b35d72070e1ee85d82bae5a


