from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def generuj(n):
    f = None
    T = [randint(1,20) for _ in range(n)]
    for i in range(n-1, -1, -1):
        tmp = Node(T[i])
        tmp.next = f
        f = tmp
    return f

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

def wypisz(f):
    while f != None:
        print(f.val, end = ' -> ')
        f = f.next
    print(f)

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

def czy_cykl(first):
    f = first
    while f != None:
        if f.next == f:
            return True
        a = first
        while a != f:
            if a == f.next:
                return True
            a = a.next
        f = f.next
    return False

first = generuj(10)
wypisz(first)
print(czy_cykl(first))

first = generuj_cykl(10, 2)
wypisz_cykl(first)
print(czy_cykl(first))