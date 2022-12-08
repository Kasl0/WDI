from math import log

def f(x):
    return x**x - 2020

def f_first_derivative(x):
    return (x**x) * (log(x) + 1)

def f_second_derivative(x):
    return (x**x) * (log(x) + 1)**2 + x**(x-1)

a = 3
b = 10
E = 0.1

z = (a + b) / 2

if f_first_derivative(z) * f_second_derivative(z) < 0:
    x = a
else:
    x = b

while abs(f(x)) > E:
    x = x - f(x)/f_first_derivative(x)

print(x)
