from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Lista:
    def __init__(self, first=None):
        self.first = first

def generuj(n):
    f = None
    T = [randint(1,20) for _ in range(n)]
    for i in range(n-1, -1, -1):
        tmp = Node(T[i])
        tmp.next = f
        f = tmp
    return Lista(f)

def wypisz(lista):
    f = lista.first
    while f != None:
        print(f.val, end = ' -> ')
        f = f.next
    print(f)

def usun_najdluzsza(lista):
    f = lista.first

    maks = 1
    maks_pocz = None
    maks_kon = lista.first
    unikalna = True

    akt = 1
    akt_pocz = None

    while f.next != None:
        if f.val < f.next.val:
            akt += 1
        else:
            if maks == akt:
                unikalna = False
            if maks < akt:
                unikalna = True
                maks = akt
                maks_pocz = akt_pocz
                maks_kon = f
            akt = 1
            akt_pocz = f

        f = f.next
    
    if maks == akt:
        unikalna = False
    if maks < akt:
        unikalna = True
        maks = akt
        maks_pocz = akt_pocz
        maks_kon = f

    if unikalna:
        if maks_pocz != None:
            maks_pocz.next = maks_kon.next
        else:
            lista.first = maks_kon.next

lista = generuj(10)
wypisz(lista)

usun_najdluzsza(lista)
wypisz(lista)