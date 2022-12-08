from random import randint

def funkcja(tablica):
    for wiersz in range(len(tablica)):
        for kolumna in range(len(tablica)):
            n = tablica[wiersz][kolumna]
            while n > 0:
                if n % 10 == 2 or n % 10 == 3 or n % 10 == 5 or n % 10 == 7:
                    break
                n //= 10
            else:
                break
        else:
            return True
    return False
    
N = int(input("N="))
T = [[randint(1,10) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])

print(funkcja(T))