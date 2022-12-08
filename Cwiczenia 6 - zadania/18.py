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

def unikalne(lista):
    prev = None
    f = lista.first

    while f != None:
        a = f
        b = f.next
        flag = 0
        while b != None:
            if f.val == b.val:
                a.next = b.next
                flag = 1
            else:    
                a = b
            b = b.next
        
        if flag and prev != None:
            prev.next = f.next
        elif flag:
            lista.first = f.next
        else:
            prev = f

        f = f.next

lista = generuj(10)
wypisz(lista)

unikalne(lista)
wypisz(lista)