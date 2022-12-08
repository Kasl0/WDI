from random import randint

def dlugosc(n):
    dl = 0
    while n > 0:
        dl += 1
        n //= 10
    return dl

N = int(input("N="))
tablica = [randint(1, 1000) for _ in range(N)]
print(tablica)

for liczba in tablica:
    for i in range(dlugosc(liczba)):
        if liczba//(10**i) % 2 == 0:
            break
    else:
        print("tak")
        exit()
print("nie")