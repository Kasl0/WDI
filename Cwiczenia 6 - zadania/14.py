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
    f = lista.first
    last_time = f

    while f.next != None:
        if f.next.val % f.val == 0:
            if f == lista.first:
                lista.first = f.next
            else:
                last_time.next = f.next
        else:
            last_time = f

        f = f.next


lista = generuj(10)
wypisz(lista)

usun(lista)
wypisz(lista)