from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def generuj(n):
    f = None
    T = [randint(0,9) for _ in range(n)]
    if T[0] == 0:
        T[0] = randint(1,9)
    for i in range(n-1, -1, -1):
        tmp = Node(T[i])
        tmp.next = f
        if f != None:
            f.prev = tmp
        f = tmp
    return f

def wypisz(f):
    print(end = 'None <- ')
    while f.next != None:
        print(f.val, end = ' <-> ')
        f = f.next
    print(f.val, end = ' -> ')
    print(f.next)

def dodaj(a, b):
    f = None
    a_first_val = a.val
    b_first_val = b.val
    while a.next != None:
        a = a.next
    while b.next != None:
        b = b.next

    dod = 0
    while a.val + b.val + dod > 0 or a.prev != None or b.prev != None:
        if a.val + b.val + dod < 10:
            tmp = Node(a.val + b.val + dod)
            dod = 0
        else:
            tmp = Node(a.val + b.val + dod - 10)
            dod = 1
        tmp.next = f
        if f != None:
            f.prev = tmp
        f = tmp

        if a.prev != None:
            a = a.prev
        else:
            a.val = 0

        if b.prev != None:
            b = b.prev
        else:
            b.val = 0
    
    a.val = a_first_val
    b.val = b_first_val

    return f

pierwsza = generuj(5)
wypisz(pierwsza)
druga = generuj(4)
wypisz(druga)

suma = dodaj(pierwsza, druga)
wypisz(suma)