from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Lista:
    def __init__(self, first=None):
        self.first = first

def generuj_cykl(n):
    f = None
    last = None
    T = [randint(1,20) for _ in range(n)]
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

def usun(lista, k):
    wsk = lista.first
    pierwszy_raz = True
    czy_usunieto = False
    flag = False
    f = wsk

    while f != wsk or pierwszy_raz:
        if ile_takich_samych(wsk, f.val) == k:

            d_pierwszy_raz = True
            d = wsk

            while d != wsk or d_pierwszy_raz:
                
                if d.next.val == f.val:

                    if d.next == wsk:
                        flag = d
                        d = d.next
                        d_pierwszy_raz = False
                    else:
                        d.next = d.next.next
                        czy_usunieto = True
                else:
                    d = d.next
                    d_pierwszy_raz = False

        f = f.next
        pierwszy_raz = False

    if flag:
        flag.next = flag.next.next
        lista.first = flag.next
        czy_usunieto = True
    
    return czy_usunieto

def ile_takich_samych(wsk, n):
    ile = (wsk.val == n)
    f = wsk.next

    while f != wsk:
        ile += (f.val == n)
        f = f.next

    return ile

lista = generuj_cykl(10)
wypisz_cykl(lista)

k = int(input("k="))
print(usun(lista, k))
wypisz_cykl(lista)