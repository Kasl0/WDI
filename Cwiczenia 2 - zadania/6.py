from math import sqrt

n = int(input("n="))
for dzielnik in range(int(sqrt(n)),n):
    if n % dzielnik == 0:
        print(dzielnik, n//dzielnik)
        break


