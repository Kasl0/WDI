a_old = 0
a = 1
b = 2

if int(input("a=")) != a_old:
    exit()

while True:
    if int(input("a=")) == a:
        print(b)
    else:
        break
    b += 2 * a_old
    a, a_old = a - b * a_old, a