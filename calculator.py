"""
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#https://github.com/mfarmer5/lab11-MF-AR
#Partner 1: Mahak Farmer
#Partner 2: Aashita Rai

# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError("a has to be greater than zero.")
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
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




