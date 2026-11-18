import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def sub(a, b):
    return subtract(a, b)


def multiply(a, b):
    return a * b


def mul(a, b):
    return multiply(a, b)


def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)


def log(a, b):
    return logarithm(a, b)


def exponent(a, b):
    return a ** b


def exp(a, b):
    return exponent(a, b)


def hypotenuse(a, b):
    return math.hypot(a, b)


def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
