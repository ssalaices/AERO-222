#1/23/24

from sympy import *

x = Symbol("x")

expression = 100 - x**3

def f(x):
    y = 100 - x**3
    return y

bracket = [1, 5]

p0 = bracket[0]
p1 = bracket[1]

secant_equation = (f(p1) - f(p0)) / (p1 - p0)