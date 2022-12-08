n = int(input("n="))

#1:
#dlugosc = len(str(n))

#2:
#from math import log10
#dlugosc = int(log10(n)) + 1

#3:
n_temp = n
dlugosc = 0
while n_temp > 0:
    dlugosc += 1
    n_temp //= 10

suma = 0
for i in range(1, 2**dlugosc):
    nowa = 0
    counter = 0
    i_temp = i
    n_temp = n
    for dl in range(0, dlugosc):
        if i_temp % 2:
            nowa += (n_temp % 10) * (10 ** counter)
            counter += 1
        n_temp //= 10
        i_temp //= 2
    if nowa % 7 == 0:
        #print(nowa)
        suma += 1

print(suma)