ciag = [0 for _ in range(100)]

ciag[0] = int(input())
dlugosc = 1
while ciag[dlugosc-1] != 0:
    ciag[dlugosc] = int(input())
    dlugosc += 1
dlugosc -= 1

for n in range(0, 10):
    min = 10**9
    for i in range(0, dlugosc):
        if ciag[i] < min:
            min = ciag[i]
    for i in range(0, dlugosc):
        if ciag[i] == min:
            ciag[i] = 10**9
            break

print(min)