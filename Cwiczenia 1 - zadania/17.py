a = int(input("a="))
b = int(input("a="))

while a < 10**6:
    a, b = a + b, a

print(a/b)