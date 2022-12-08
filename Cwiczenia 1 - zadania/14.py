from math import factorial

x = float(input("x="))
cos = 0
i = 0

while i < 100:
    cos += (1/factorial(i))*(x**i)
    i += 2
    cos -= (1/factorial(i))*(x**i)
    i += 2

print(cos)
