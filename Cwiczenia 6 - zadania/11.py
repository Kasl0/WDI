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
    T = [randint(1,50) for _ in range(n)]
    T = list(dict.fromkeys(T))
    n = len(T)
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

def funkcja(lista, k):
    f = lista.first
    prev = None
    while f != None:
        if f.val == k:
            if prev != None:
                prev.next = f.next
            else:
                lista.first = f.next
            del f
            return

        prev = f
        f = f.next
    
    tmp = Node(k)
    prev.next = tmp

lista = generuj(20)
wypisz(lista)

klucz = int(input("klucz="))
funkcja(lista, klucz)
wypisz(lista)