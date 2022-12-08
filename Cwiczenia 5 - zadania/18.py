from random import randint

def dlugosc(n):
    dl = 0
    while n > 0:
        n //= 10
        dl += 1
    return dl

def czy_moze(w, k, B=[[0 for _ in range(8)] for _ in range(8)]):
    B[w][k] = 1
    if w == 7 and k == 7:
        #for i in range(8):
        #    print(B[i])
        return True

    return (w+1 < 8 and B[w+1][k] == 0 and T[w][k]%10 < T[w+1][k]/10**(dlugosc(T[w+1][k])-1) and czy_moze(w+1,k,B)) or (k+1 < 8 and B[w][k+1] == 0 and T[w][k]%10 < T[w][k+1]/10**(dlugosc(T[w][k+1])-1) and czy_moze(w,k+1,B)) or (w+1 < 8 and k+1 < 8 and B[w+1][k+1] == 0 and T[w][k]%10 < T[w+1][k+1]/10**(dlugosc(T[w+1][k+1])-1) and czy_moze(w+1,k+1,B)) or (w+1 < 8 and k > w and B[w+1][k-1] == 0 and T[w][k]%10 < T[w+1][k-1]/10**(dlugosc(T[w+1][k-1])-1) and czy_moze(w+1,k-1,B)) or (k+1 < 8 and w > k and B[w-1][k+1] == 0 and T[w][k]%10 < T[w-1][k+1]/10**(dlugosc(T[w-1][k+1])-1) and czy_moze(w-1,k+1,B))


T = [[randint(1,1000) for _ in range(8)] for _ in range(8)]

for i in range(8):
    print(T[i])

print(czy_moze(0, 0))
