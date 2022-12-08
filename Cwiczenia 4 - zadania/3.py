from random import randint

def funkcja(tablica):
    for wiersz in tablica:
        istnieje = True
        for liczba in wiersz:
            while liczba > 0:
                if liczba % 2 == 0:
                    break
                liczba //= 10
            else:
                istnieje = False
                break
        if istnieje:
            return True
    return False

N = int(input("N="))
T = [[randint(1,100) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])
    
print(funkcja(T))