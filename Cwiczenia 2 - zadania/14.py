def dlugosc(n):
    dl = 0
    while n > 0:
        dl += 1
        n //= 10
    return dl

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

a = int(input("a="))
b = int(input("b="))
a, b = max(a, b), min(a, b)
a_dl = dlugosc(a)
b_dl = dlugosc(b)
ile_pierwszych = 0

for i in range(1, (b_dl+1)**(a_dl+1)):
    liczba = 0
    i_temp = i
    a_counter = 1
    b_counter = 1
    counter = 0
    for dl in range(0, a_dl + 1):
        ile = i_temp % (b_dl+1)
        counter += ile
        while ile > 0:
            liczba *= 10
            liczba += b//(10**(b_dl-b_counter))%10
            b_counter += 1
            ile -= 1
        if dl == a_dl:
            break
        liczba *= 10
        liczba += a//(10**(a_dl-a_counter))%10
        a_counter += 1
        i_temp //= (b_dl+1)
    if b_dl == counter and czy_pierwsza(liczba):
        ile_pierwszych += 1
        
print(ile_pierwszych)