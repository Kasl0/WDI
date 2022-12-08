from random import randint

def dlugosc(n):
    dl = 0
    while n > 0:
        n //= 10
        dl += 1
    return dl

def start(w, k):
    B=[[1 for _ in range(8)] for _ in range(8)]
    B[w][k] = 2*3*5*7

    for now_w, now_k in ((w,k+1),(w-1,k+1),(w-1,k),(w-1,k-1),(w+1,k+1)):
        if now_w == w-1 and now_k == k-1 and not 7 < w+k:
            continue
        if now_w == w+1 and now_k == k+1 and not w+k < 7:
            continue
        if czy_moze(now_w, now_k, w, k, B, 2):
            return True

    for now_w, now_k in ((w,k-1),(w-1,k),(w-1,k-1),(w+1,k-1),(w-1,k+1)):
        if now_w == w+1 and now_k == k-1 and not k > w:
            continue
        if now_w == w-1 and now_k == k+1 and not w > k:
            continue
        if czy_moze(now_w, now_k, w, k, B, 3):
            return True

    for now_w, now_k in ((w,k-1),(w+1,k),(w+1,k-1),(w-1,k-1),(w+1,k+1)):
        if now_w == w-1 and now_k == k-1 and not 7 < w+k:
            continue
        if now_w == w+1 and now_k == k+1 and not w+k < 7:
            continue
        if czy_moze(now_w, now_k, w, k, B, 5):
            return True
    
    for now_w, now_k in ((w+1,k+1),(w+1,k),(w,k+1),(w+1,k-1),(w-1,k+1)):
        if now_w == w+1 and now_k == k-1 and not k > w:
            continue
        if now_w == w-1 and now_k == k+1 and not w > k:
            continue
        if czy_moze(now_w, now_k, w, k, B, 7):
            return True

def czy_moze(w, k, ost_w, ost_k, B, gdzie):
    if 0 <= w < 8 and 0 <= k < 8 and B[w][k]%gdzie != 0 and T[w][k]%10 < T[ost_w][ost_k]/10**(dlugosc(T[ost_w][ost_k])-1):
        B[w][k] *= gdzie
        if ((w,k) == (0,0) and B[w][k]%3 == 0) or ((w,k) == (0,7) and B[w][k]%2 == 0) or ((w,k) == (7,0) and B[w][k]%5 == 0) or ((w,k) == (7,7) and B[w][k]%7 == 0):
            for i in range(8):
                print(B[i])
            return True

        if gdzie == 2:
            for now_w, now_k in ((w,k+1),(w-1,k+1),(w-1,k),(w-1,k-1),(w+1,k+1)):
                if now_w == w-1 and now_k == k-1 and not 7 < w+k:
                    continue
                if now_w == w+1 and now_k == k+1 and not w+k < 7:
                    continue
                if czy_moze(now_w, now_k, w, k, B, 2):
                    return True

        elif gdzie == 3:
            for now_w, now_k in ((w,k-1),(w-1,k),(w-1,k-1),(w+1,k-1),(w-1,k+1)):
                if now_w == w+1 and now_k == k-1 and not k > w:
                    continue
                if now_w == w-1 and now_k == k+1 and not w > k:
                    continue
                if czy_moze(now_w, now_k, w, k, B, 3):
                    return True

        elif gdzie == 5:
            for now_w, now_k in ((w,k-1),(w+1,k),(w+1,k-1),(w-1,k-1),(w+1,k+1)):
                if now_w == w-1 and now_k == k-1 and not 7 < w+k:
                    continue
                if now_w == w+1 and now_k == k+1 and not w+k < 7:
                    continue
                if czy_moze(now_w, now_k, w, k, B, 5):
                    return True

        elif gdzie == 7:
            for now_w, now_k in ((w+1,k+1),(w+1,k),(w,k+1),(w+1,k-1),(w-1,k+1)):
                if now_w == w+1 and now_k == k-1 and k <= w:
                    continue
                if now_w == w-1 and now_k == k+1 and w <= k:
                    continue
                if czy_moze(now_w, now_k, w, k, B, 7):
                    return True

T = [[randint(1,1000) for _ in range(8)] for _ in range(8)]

for i in range(8):
    print(T[i])

print(start(3, 3))
