class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def stworz(n):
    f = None
    for _ in range(n):
        tmp = Node(0)
        tmp.next = f
        f = tmp
    return f

def wypisz(f):
    while f != None:
        print(f.val, end = ' -> ')
        f = f.next
    print(f)

def wartosc(f, n):
    while f != None:
        if n==0:
            return f.val
        n -= 1
        f = f.next

def podstaw(f, value, n):
    while f != None:
        if n==0:
            f.val = value
        n -= 1
        f = f.next

tab = stworz(5)
wypisz(tab)

podstaw(tab, 3, 3)
wypisz(tab)

print(wartosc(tab, 3))