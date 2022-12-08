from random import randint

def sprawdz(ind):
    if ind < N and pola[ind] == False:
        if ind == N-1:
            print("tak")
            exit()
        b = 2
        n = tablica[ind]
        while n > 1 and b*b <= n:
            if n % b == 0:
                sprawdz(ind+b)
                n //= b
            else:
                b += 1
        if n > 1:
            sprawdz(ind+n)
        pola[ind] = True


N = int(input("N="))
tablica = [randint(1, 1000) for _ in range(N)]
pola = [False for _ in range(N)]
print(tablica)
sprawdz(0)
print("nie")