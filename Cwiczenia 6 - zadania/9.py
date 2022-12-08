from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def generuj(n):
    f = None
    T = [randint(0,9) for _ in range(n)]
    if T[0] == 0:
        T[0] = randint(1,9)
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

def zwieksz(first):
    f = first
    k = 0

    while f.next != None:
        f = f.next
        k += 1

    f.val += 1
    while f.val == 10:
        f.val = 0

        if f == first:
            ost = 1
            while f.next != None:
                f.val, ost = ost, f.val
                f = f.next
            f.val, ost = ost, f.val
            f.next = Node(ost)
            return

        f = first
        k -= 1
        for _ in range(k):
            f = f.next
        f.val += 1

first = generuj(10)
wypisz(first)

zwieksz(first)
wypisz(first)