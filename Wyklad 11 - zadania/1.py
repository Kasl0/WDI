from random import randint

def find(tab, el, p, k):
    if p > k:
        return -1

    p1 = p + (k - p) // 3
    p2 = p + (k - p) * 2 // 3

    if tab[p1] == el:
        return p1
    if tab[p2] == el:
        return p2

    if el < tab[p1]:
        return find(tab, el, p, p1-1)
    if tab[p2] < el:    
        return find(tab, el, p2+1, k)
    return find(tab, el, p1+1, p2-1)

T = [randint(1,20) for _ in range(10)]
T.sort()
print(T)

print(find(T, int(input("find = ")), 0, len(T)-1))