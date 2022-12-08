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

def rozdziel(f):
    listy = [None for _ in range(10)]
    while f != None:

        tmp = Node(f.val)
        tmp.next = listy[f.val % 10]
        listy[f.val % 10] = tmp

        f = f.next

    #for i in range(10):
    #    wypisz(listy[i])

    first = None
    f = None
    
    for i in range(10):
        if first == None and listy[i] != None:
            first = listy[i]
        if listy[i] != None:
            if f != None:
                f.next = listy[i]
            f = listy[i]
            while f.next != None:
                f = f.next

    return first

first = generuj(10)
wypisz(first)
wypisz(rozdziel(first))