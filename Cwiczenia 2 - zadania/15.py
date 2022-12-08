N = int(input("N="))

for liczba in range(10**(N-1),10**N):
    n = liczba
    suma = 0
    while n > 0:
        suma += (n % 10)**N
        n //= 10
    if suma == liczba:
        print(liczba)