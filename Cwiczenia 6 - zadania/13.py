from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def generuj(n):
    f = None
    T = [randint(-100,100) for _ in range(n)]
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
    prev = f
    last_time = f
    f = f.next

    while f != None:
        if prev.val > f.val:
            last_time.next = f.next
        else:
            last_time = f

        prev = f
        f = f.next


first = generuj(10)
wypisz(first)

usun(first)
wypisz(first)