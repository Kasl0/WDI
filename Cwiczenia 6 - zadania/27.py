from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def generuj(n):
    f = None
    T = [randint(1,100) for _ in range(n)]
    T.sort()
    for i in range(n-1, -1, -1):
        tmp = Node(T[i])
        tmp.next = f
        f = tmp
    return f

def wypisz(f):
    while f != None:
        print(f.val, end = ' -> ')
        f = f.next
    print(f)

def scal_iter(a, b):
    prev = None
    first = None

    while a != None or b != None:
        if b == None:
            tmp = Node(a.val)
            a = a.next
        elif a == None:
            tmp = Node(b.val)
            b = b.next
        elif a.val < b.val:
            tmp = Node(a.val)
            a = a.next
        else:
            tmp = Node(b.val)
            b = b.next

        if prev != None:
            prev.next = tmp
        else:
            first = tmp
        prev = tmp

    return first

def scal_rek(a, b, prev=None):
    if a == None and b == None:
        return

    if b == None:
        tmp = Node(a.val)
        a = a.next
    elif a == None:
        tmp = Node(b.val)
        b = b.next
    elif a.val < b.val:
        tmp = Node(a.val)
        a = a.next
    else:
        tmp = Node(b.val)
        b = b.next
    
    first = None

    if prev != None:
        prev.next = tmp
    else:
        first = tmp

    scal_rek(a, b, tmp)

    return first

pierwsza = generuj(3)
druga = generuj(2)
wypisz(pierwsza)
wypisz(druga)

scalona = scal_iter(pierwsza, druga)
wypisz(scalona)

scalona = scal_rek(pierwsza, druga)
wypisz(scalona)
