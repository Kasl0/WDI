from random import randint

def find(tab, el, p, k):
    if p > k:
        return -1

    if p == 0:
        znak = ord(el[0])-97
        sr = p + (k - p) * znak // 25
    else:
        sr = p + k // 2

    if tab[sr] == el:
        return sr

    if el < tab[sr]:
        return find(tab, el, p, sr-1)
    return find(tab, el, sr+1, k)

T = [chr(randint(97,122))+chr(randint(97,122))+chr(randint(97,122)) for _ in range(10)]
T.sort()
print(T)

print(find(T, input("find = "), 0, len(T)-1))