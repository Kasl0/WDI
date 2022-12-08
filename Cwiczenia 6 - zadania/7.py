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

def usun(f):
    prev = None

    while f.next != None:
        prev = f
        f = f.next

    if prev != None:
        prev.next = None
    del f

first = generuj(5)
wypisz(first)

usun(first)
wypisz(first)