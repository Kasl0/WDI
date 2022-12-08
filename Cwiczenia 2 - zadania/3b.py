def czy_palindrom(n, system):
    save = n
    new = 0
    while n > 0:
        new *= system
        new += n%system
        n //= system
    return new == save

n = int(input("n="))

print(czy_palindrom(n, 10))
print(czy_palindrom(n, 2))