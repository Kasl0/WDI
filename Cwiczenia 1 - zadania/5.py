liczba = float(input("num="))
a = 1
b = 2

while abs(a-b) > 0.000000001:
    a, b = (liczba/a + a)/2, a

print(a)