from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Lista:
    def __init__(self, first=None):
        self.first = first

def generuj(n):
    f = None
    T = [randint(1,100) for _ in range(n)]
    for i in range(n-1, -1, -1):
        tmp = Node(T[i])
        tmp.next = f
        if f != None:
            f.prev = tmp
        f = tmp
    return Lista(f)

def wypisz(lista):
    f = lista.first
    print(end = 'None <- ')
    while f.next != None:
        print(f.val, end = ' <-> ')
        f = f.next
    print(f.val, end = ' -> ')
    print(f.next)

def usun(lista):
    f = lista.first

    while f != None:
        if czy_nieparzysta_ilosc(f.val):
            if f.prev != None:
                f.prev.next = f.next
                if f.next != None:
                    f.next.prev = f.prev
            else:
                lista.first = f.next
                f.next.prev = None

        f = f.next

def czy_nieparzysta_ilosc(k):
    jedynek = 0

    while k > 0:
        jedynek += k % 2
        k /= 2
        
    return (jedynek % 2)

lista = generuj(10)
wypisz(lista)

usun(lista)
wypisz(lista)