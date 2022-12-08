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

def wstaw(z, nap):
    f = z.first
    prev = None

    while f != None and f.val < nap:
        prev = f
        f = f.next

    if f != None and f.val == nap:
        return False

    tmp = Node(nap)
    tmp.next = f
    if prev != None:
        prev.next = tmp
    else:
        z.first = tmp
    
    return True

zbior = Zbior()
wstaw(zbior, "ff")
wstaw(zbior, "bb")
wstaw(zbior, "dd")
wstaw(zbior, "zz")
wstaw(zbior, "aa")

wypisz(zbior)

wstaw(zbior, "ee")
wypisz(zbior)