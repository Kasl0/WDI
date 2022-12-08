from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Lista:
    def __init__(self, first=None):
        self.first = first

def generuj_cykl():
    f = None
    last = None
    T = ["bartek", "leszek", "marek", "ola", "zosia"]
    n = len(T)
    for i in range(n-1, -1, -1):
        tmp = Node(T[i])

        if last == None:
            last = tmp
        
        tmp.next = f
        f = tmp

    last.next = f
    
    return Lista(f)

def wypisz_cykl(lista):
    f = lista.first

    print(f.val, end = ' -> ')
    f = f.next

    while f != lista.first:
        print(f.val, end = ' -> ')
        f = f.next

    print("first")

def wstaw(lista, napis):
    f = lista.first
    pierwszy_raz = True

    while f != lista.first or pierwszy_raz:

        if f.val[-1] < napis[0] and f.next.val[0] > napis[-1]:
            tmp = Node(napis)
            tmp.next = f.next
            f.next = tmp

            lista.first = tmp

            return True

        f = f.next
        pierwszy_raz = False

    return False

lista = generuj_cykl()
wypisz_cykl(lista)

napis = input("napis=")
print(wstaw(lista, napis))
wypisz_cykl(lista)