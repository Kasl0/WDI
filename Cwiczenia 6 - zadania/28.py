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
    T = [randint(1,10) for _ in range(n)]
    T = list(dict.fromkeys(T))
    n = len(T)
    for i in range(n-1, -1, -1):
        tmp = Node(T[i])
        tmp.next = f
        f = tmp
    return Lista(f)

def generuj_z_sortem(n):
    f = None
    T = [randint(1,10) for _ in range(n)]
    T = list(dict.fromkeys(T))
    n = len(T)
    T.sort()
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

def usun_z_obu(pierwsza, druga):
    ile = 0
    d_prev = None
    d = druga.first
    
    while d != None:

        p_prev = None
        p = pierwsza.first

        while p != None and p.val < d.val:
            p_prev = p
            p = p.next

        if p != None and p.val == d.val:
            ile += 1

            if p_prev != None:
                p_prev.next = p.next
            else:
                pierwsza.first = p.next
            
            if d_prev != None:
                d_prev.next = d.next
            else:
                druga.first = d.next

        else:
            d_prev = d

        d = d.next
    
    return ile

pierwsza = generuj_z_sortem(10)
druga = generuj(5)
wypisz(pierwsza)
wypisz(druga)

print(usun_z_obu(pierwsza, druga))
wypisz(pierwsza)
wypisz(druga)
