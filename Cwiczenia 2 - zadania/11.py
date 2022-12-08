n = int(input("n="))
old = n % 10
n //= 10

while n > 0:
    if old <= n % 10:
        print("nie")
        exit()
    old = n % 10
    n //= 10
print("tak")