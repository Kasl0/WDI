num = int(input("num="))
a = 1
b = 1

while a < 10**6:
    if a*b == num:
        print("yes")
        exit()
    a, b = a + b, a

print("no")