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

def wstaw(f, n):
    while f.next != None:
        f = f.next
    f.next = Node(n)

first = generuj(5)
wypisz(first)

wstaw(first, 8)
wypisz(first)