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
    T = [randint(1,100) for _ in range(n)]
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

def odwroc(lista):
    f = lista.first
    prev = None
    prevprev = None

    while f != None:
        if prev != None:
            prev.next = prevprev

        prevprev = prev
        prev = f
        f = f.next

    if prev != None:
        prev.next = prevprev
    lista.first = prev

lista = generuj(5)
wypisz(lista)

odwroc(lista)
wypisz(lista)
