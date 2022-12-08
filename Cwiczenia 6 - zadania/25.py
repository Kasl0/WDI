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

def wskaznik_przed_cyklem(first):
    prev = None
    f = first
    while True:

        if f.next == f:
            return prev

        a_prev = None
        a = first

        while a != f:
            if a == f.next:
                return a_prev
            
            a_prev = a
            a = a.next

        prev = f
        f = f.next

first = generuj_cykl(10, 2)
wypisz_cykl(first)
print(wskaznik_przed_cyklem(first).val)