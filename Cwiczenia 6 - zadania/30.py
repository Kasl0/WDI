from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def generuj(n):
    f = None
    T = [randint(1,10) for _ in range(n)]
    T = list(dict.fromkeys(T))
    n = len(T)
    for i in range(n-1, -1, -1):
        tmp = Node(T[i])
        tmp.next = f
        f = tmp
    return f

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
    return f

def wypisz(f):
    while f != None:
        print(f.val, end = ' -> ')
        f = f.next
    print(f)

def suma_mnogosciowa(pierwsza, druga):
    first = None
    prev = None

    while pierwsza != None:

        tmp = Node(pierwsza.val)

        if first == None:
            first = tmp

        if prev != None:
            prev.next = tmp

        prev = tmp

        pierwsza = pierwsza.next
    
    while druga != None:
        f_prev = None
        f = first
        tmp = Node(druga.val)

        while f != None and f.val < druga.val:
            f_prev = f
            f = f.next

        if f == None:
            f_prev.next = tmp

        elif f.val > druga.val:

            if f_prev != None:
                f_prev.next = tmp
                tmp.next = f
            else:
                tmp.next = first
                first = tmp
                
        druga = druga.next

    return first

pierwsza = generuj_z_sortem(10)
druga = generuj(5)
wypisz(pierwsza)
wypisz(druga)

suma = suma_mnogosciowa(pierwsza, druga)
wypisz(suma)
