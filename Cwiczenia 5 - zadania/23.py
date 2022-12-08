from random import randint

def wybierz(T, R, i=0, wybrane=()):
    if len(wybrane) == 3:
        return wypadkowa(wybrane, R)
    if i == len(T):
        return False

    return wybierz(T, R, i+1, wybrane+(T[i],)) or wybierz(T, R, i+1, wybrane)

def wypadkowa(wybrane, R):
    r1, r2, r3 = wybrane
    if r1 + r2 + r3 == R:
        return True
    if 1/R == 1/r1 + 1/r2 + 1/r3:
        return True
    if R == (r1 * r2) / (r1 + r2) + r3 or R == (r1 * r3) / (r1 + r3) + r2 or R == (r2 * r3) / (r2 + r3) + r1:
        return True
    return False

N = int(input("N="))
T = [randint(1,100) for _ in range(N)]
print(T)

R = int(input("R="))
print(wybierz(T, R))