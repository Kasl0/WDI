liczba = float(input("num="))
a = 1
b = 2

while abs(a-b) > 0.000000001:
    a, b = (2*a + liczba/a**2)/3, a

print(a)