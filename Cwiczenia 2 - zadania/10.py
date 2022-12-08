n = int(input("n="))
A = 2

while n >= A:
    if n % A == 0:
        print("tak")
        exit()
    A = 3*A + 1
print("nie")