from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def generuj(n):
    f = None
    T = [randint(1,100) for _ in range(n)]
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

def czy_zawiera_sie(a, b):

    aa = a
    a_dl = 0
    while aa != None:
        a_dl += 1
        aa = aa.next

    bb = b
    b_dl = 0
    while bb != None:
        b_dl += 1
        bb = bb.next

    if a_dl < b_dl:
        a, b = b, a
    
    aa = a
    bb = b
    lista = False
    while aa != None:

        if aa.val == bb.val and (lista or bb == b):
            bb = bb.next
            lista = True
        else:
            bb = b
            lista = False

        aa = aa.next

        if bb == None:
            return True

    return False

pierwsza = generuj(5)
druga = generuj(1)
wypisz(pierwsza)
wypisz(druga)

print(czy_zawiera_sie(pierwsza, druga))