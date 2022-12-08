from random import randint

def czy_pierwsza(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i**2 <= n:
        if n%i == 0:
            return False
        i += 2
    return True

def funkcja(t1,t2):
    czy_byla = [0 for _ in range(10**6)]
    ile = 0
    for i in range(2**N):
        for j in range(2**N):
            i_temp = i
            j_temp = j
            suma = 0
            for dl in range(N):
                if i_temp%2 == 0  and j_temp%2 == 0:
                    break
                if i_temp%2:
                    suma += t1[dl]
                if j_temp%2:
                    suma += t2[dl]
                j_temp //= 2
                i_temp //= 2
            else:
                if czy_pierwsza(suma) and czy_byla[suma] == 0:
                        print(suma)
                        ile += 1
                        czy_byla[suma] += 1
    return ile

N = int(input("N="))
t1 = [randint(1, 10) for _ in range(N)]
t2 = [randint(1, 10) for _ in range(N)]
print(t1)
print(t2)
print(funkcja(t1,t2))