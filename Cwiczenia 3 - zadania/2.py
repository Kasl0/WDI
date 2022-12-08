ile = [0 for _ in range(10)]

a = int(input("a="))
b = int(input("b="))

while a > 0:
    ile[a % 10] += 1
    a //= 10

while b > 0:
    ile[b % 10] -= 1
    b //= 10

if ile == [0] * 10:
    print("tak")
else:
    print("nie")