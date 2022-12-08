n = int(input("n="))

n_temp = n
dlugosc = 0
while n_temp > 0:
    dlugosc += 1
    n_temp //= 10

if dlugosc > 9:
    print("nie")
else:
    while n > 0:
        if n % 10 == dlugosc:
            print("tak")
            exit()
        n //= 10
print("nie")