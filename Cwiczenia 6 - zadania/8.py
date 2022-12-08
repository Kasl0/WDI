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

def usun_co_drugi(f):
    prev = None
    k = 0

    while f != None:

        if k % 2 and prev != None:
            prev.next = f.next

        prev = f
        f = f.next
        k += 1

first = generuj(10)
wypisz(first)

usun_co_drugi(first)
wypisz(first)