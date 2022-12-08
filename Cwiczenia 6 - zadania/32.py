from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def generuj(n):
    f = None
    T = [randint(-10,10) for _ in range(n)]
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

def roznica_wielomianow(a, b):
    first = None

    while a != None or b != None:

        if a == None:
            tmp = Node(-b.val)
            b = b.next
        elif b == None:
            tmp = Node(a.val)
            a = a.next
        else:
            tmp = Node(a.val - b.val)
            a = a.next
            b = b.next

        if first == None:
            first = tmp
            f = first
        else:
            f.next = tmp
            f = f.next

    return first

pierwszy = generuj(10)
drugi = generuj(5)
wypisz(pierwszy)
wypisz(drugi)

wynikowy = roznica_wielomianow(pierwszy, drugi)
wypisz(wynikowy)
