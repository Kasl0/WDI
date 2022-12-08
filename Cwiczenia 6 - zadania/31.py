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

def rozdziel(first, pierwsza, druga):
    while pierwsza.next != None:
        pierwsza = pierwsza.next

    while druga.next != None:
        druga = druga.next

    ile = 0
    while first != None:
        if first.val > 0 and first.val % 2 == 0:

            if pierwsza.val == 0:
                pierwsza.val = first.val
            else:
                pierwsza.next = Node(first.val)
                pierwsza = pierwsza.next

        elif first.val < 0 and first.val % 2 == 1:

            if druga.val == 0:
                druga.val = first.val
            else:
                druga.next = Node(first.val)
                druga = druga.next
        
        else:
            ile += 1

        first = first.next

    return ile

first = generuj(10)
wypisz(first)

parzyste_dodatnie = Node(0)
nieparzyste_ujemne = Node(0)
print(rozdziel(first, parzyste_dodatnie, nieparzyste_ujemne))
wypisz(parzyste_dodatnie)
wypisz(nieparzyste_ujemne)
