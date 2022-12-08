from random import randint

def czy_mozna(T, k, a=0, b=0, p=0):
    if p == len(T):
        if a == b and k == 0:
            return True
        return False

    if k < 0 or k > len(T)-p:
        return False

    return czy_mozna(T, k, a, b, p+1) or czy_mozna(T, k-1, a+T[p], b, p+1) or czy_mozna(T, k-1, a, b+T[p], p+1)

N = int(input("N="))
T = [randint(1,100) for _ in range(N)]
print(T)
k = int(input("k="))

print(czy_mozna(T, k))