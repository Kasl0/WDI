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

def ile_pierwszych(a, b, apoz=0, bpoz=0, zbud=""):
    ile = 0
    if apoz == len(a) and bpoz == len(b):
        return czy_pierwsza(int(zbud))
    if apoz < len(a):
        ile += ile_pierwszych(a, b, apoz+1, bpoz, zbud+a[apoz])
    if bpoz < len(b):
        ile += ile_pierwszych(a, b, apoz, bpoz+1, zbud+b[bpoz])
    return ile

a = input("a=")
b = input("b=")
print(ile_pierwszych(a, b))