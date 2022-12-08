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

def przenies(lista):
    prev = None
    f = lista.first

    while f != None:
        if czy_parzysta_ilosc(f.val) and prev != None:
            prev.next = f.next

            f.next = lista.first
            lista.first = f
            
            f = prev.next
        else:
            prev = f
            f = f.next

def czy_parzysta_ilosc(k):
    piatek = 0

    while k > 0:
        if k % 8 == 5:
            piatek += 1 
        k /= 8
        
    return (not (piatek % 2))

lista = generuj(10)
wypisz(lista)

przenies(lista)
wypisz(lista)