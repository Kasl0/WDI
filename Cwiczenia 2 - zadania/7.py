n = int(input("n="))
i = 0
A = i*i + i + 1

while n >= A:
    A = i*i + i + 1
    if n % A == 0:
        print("tak")
        exit()
    i += 1
print("nie")