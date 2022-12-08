from math import sqrt

m = int(input("m="))
n = int(input("n="))

suma = 0
liczba = sqrt(m) % 1

while n > 0:
    liczba *= 10
    suma += int(liczba % 10)
    n -= 1
    
print(suma)