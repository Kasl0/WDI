znaki = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

def zamiana(n, podstawa):
    dlugosc = 0
    n_save = n
    while n > 0:
        dlugosc += 1
        n //= podstawa

    n = n_save
    nowa = [0 for _ in range(dlugosc)]
    
    for i in range(0, dlugosc):
        nowa[i] = znaki[n % podstawa]
        n //= podstawa
        
    for i in range(1, dlugosc+1):
        print(nowa[dlugosc-i], end="")
    print()

n = int(input("n="))
for podst in range(2,17):
    print(podst, ": ", end="", sep="")
    zamiana(n, podst)