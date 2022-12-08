from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def generuj_cykl(n, poz):
    f = None
    last = None
    T = [randint(1,20) for _ in range(n)]
    for i in range(n-1, -1, -1):
        tmp = Node(T[i])

        if last == None:
            last = tmp
        
        tmp.next = f

        if poz == i:
            last.next = tmp

        f = tmp
    
    return f

def wypisz_cykl(first):
    f = first

    while True:
        print(f.val, end = ' -> ')

        if f.next == f:
            print(f"pozycja ostatnia ({f.val})")
            return

        a = first
        poz = 0

        while a != f:

            if a == f.next:
                print(f"pozycja {poz} ({f.next.val})")
                return

            poz += 1
            a = a.next
            
        f = f.next

def dlugosc_cyklu(first):
    f = first
    f_dl = 1
    while True:

        if f.next == f:
            return 1

        a = first
        a_dl = 0

        while a != f:
            if a == f.next:
                return f_dl - a_dl

            a_dl += 1
            a = a.next

        f_dl += 1
        f = f.next

first = generuj_cykl(10, 2)
wypisz_cykl(first)
print(dlugosc_cyklu(first))