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

def usun(lista):
    prev = None
    f = lista.first

    while f != None:
        if czy_wiecej_jedynek(f.val):
            if prev != None:
                prev.next = f.next
            else:
                lista.first = f.next

        prev = f
        f = f.next

def czy_wiecej_jedynek(k):
    jedynek = 0
    dwojek = 0

    while k > 0:
        if k % 3 == 1:
            jedynek += 1
        elif k % 3 == 2:
            dwojek += 1    
        k /= 3
        
    return jedynek > dwojek

lista = generuj(10)
wypisz(lista)

usun(lista)
wypisz(lista)