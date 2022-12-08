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
    T.sort()
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

def usun_nieunikalne(lista):
    prev = None
    f = lista.first

    ile = 0
    ost = None

    while f != None:
        if (f.next != None and f.next.val == f.val) or (ost == f.val):
            ost = f.val
            ile += 1

            if prev != None:
                prev.next = f.next
            else:
                lista.first = f.next
                
        else:
            prev = f

        f = f.next

    return ile

lista = generuj(10)
wypisz(lista)

print(usun_nieunikalne(lista))
wypisz(lista)