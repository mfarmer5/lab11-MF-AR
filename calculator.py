"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a + b
def sub(a,b ):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if a == 0:
        raise ValueError("Can't divide by zero.")
    return b/a
def log(a,b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be greater than zero and not equal to one")
    if b <= 0:
        raise ValueError("b must be greater than zero.")
    return  math.log(b, a)
def exp(a, b):
    return a ** b




