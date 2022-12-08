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
    T = [[randint(1,10), randint(11,20)] for _ in range(n)]
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

def zredukuj(lista):
    prev = None
    f = lista.first

    while f != None:
        usunieto = False
        a = f.next
        while a != None:

            if a.val[0] <= f.val[1] <= a.val[1] or a.val[0] <= f.val[0] <= a.val[1]:
                a.val = [min(a.val[0], f.val[0]), max(a.val[1], f.val[1])]
                
                if prev != None:
                    prev.next = f.next
                else:
                    lista.first = f.next
                usunieto = True

                break
            a = a.next

        if usunieto == False:
            prev = f
        f = f.next

lista = generuj(5)
wypisz(lista)

zredukuj(lista)
wypisz(lista)