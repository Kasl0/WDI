from math import sqrt

a = float(input("a="))
b = float(input("b="))

for n in range(0,10**6):
    a, b = sqrt(a*b), (a+b)/2.0

print(a)