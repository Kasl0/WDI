#KOLOKWIUM 2021

def dlugosc(n):
    dlugosc=0
    while n>0:
        dlugosc+=1
        n//=10
    return dlugosc

def czy_pierwsza(n):
    if n==2:
        return True

    if n%2==0 or n<2:
        return False

    k=3
    while k*k<=n:
        if n%k==0:
            return False
        k+=2
    return True


def czy_rozne_cyfry(n):
    cyfry=[0 for _ in range (10)]

    while n>0:
        cyfry[n%10]+=1
        n//=10

    for i in range (10):
        if cyfry[i]>1:
            return False
    return True

if __name__ == '__main__':

    liczba=int(input())
    dl=dlugosc(liczba)

    maks=0

    for i in range (0, dl+1):  #przód
        for j in range (i):  #tył
            tmp = (liczba % (10**i)) // (10**j)
            if czy_pierwsza(tmp) and czy_rozne_cyfry(tmp) and tmp>maks:
                maks = tmp
    print(maks)





#2
def zamiana(n):
    dlugosc = 0
    tmp=n

    while n > 0:
        dlugosc += 1
        n //= 4

    n=tmp
    tab=[0 for i in range (dlugosc)]

    for i in range (dlugosc):
        tab[i] = n % 4
        n //= 4

    liczba = 0
    tab=tab[::-1]
    for i in range(len(tab)):
        liczba *= 10
        liczba += tab[i]

    return liczba

def czy_takie_same_cyfry(n, m):
    cyfry=[0 for _ in range (10)]
    cyfry2=[0 for _ in range (10)]

    while n > 0:
        if cyfry[n % 10] == 1:
            break
        else:
            cyfry[n % 10] += 1
        n //= 10

    while m > 0:
        if cyfry2[m % 10] == 1:
            break
        else:
            cyfry2[m % 10] += 1
        m //= 10

    flag=True
    for i in range (10):
        if cyfry[i]!=cyfry2[i]:
            flag=False
    return flag

if __name__ == '__main__':
    t=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 38]

    maks=0
    for i in range (len(t)):
        dlugosc=0
        z1=zamiana(t[i])
        for j in range (len(t)):
            z2=zamiana(t[j])
            if czy_takie_same_cyfry(z1, z2):
                dlugosc+=1
            if dlugosc>maks:
                maks=dlugosc
    print(maks)





