class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Zbior:
    def __init__(self):
        self.first = None

def wypisz(z):
    f = z.first
    while f != None:
        print(f.val, end = ' -> ')
        f = f.next
    print(f)

def czy_nalezy(z, n):
    f = z.first

    while f != None and f.val < n:
        f = f.next

    return f != None and f.val == n

def wstaw(z, n):
    f = z.first
    prev = None

    while f != None and f.val < n:
        prev = f
        f = f.next

    if f != None and f.val == n:
        return

    tmp = Node(n)
    tmp.next = f
    if prev != None:
        prev.next = tmp
    else:
        z.first = tmp

def usun(z, n):
    f = z.first
    prev = None

    while f != None and f.val < n:
        prev = f
        f = f.next

    if f != None and f.val == n:
        if prev != None:
            prev.next = f.next
        else:
            z.first = f.next
        del f


zbior = Zbior()
wstaw(zbior, 1)
wstaw(zbior, 2)
wstaw(zbior, 3)
wstaw(zbior, 5)
wstaw(zbior, 7)

wypisz(zbior)
print(czy_nalezy(zbior, 7))

wstaw(zbior, 4)
wypisz(zbior)

usun(zbior, 2)
wypisz(zbior)