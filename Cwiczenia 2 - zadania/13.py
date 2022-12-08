n = int(input("n="))
ostatnia = n % 10
n //= 10

while n > 0:
        if n % 10 == ostatnia:
            print("nie")
            exit()
        n //= 10
print("tak")