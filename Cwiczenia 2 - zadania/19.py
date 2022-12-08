a = int(input("a="))
b = int(input("b="))
a_save = a
b_save = b
min_pos = 9999999
min_i = 0

print(a//b, end=".")

for i in range(0,100):
    a = a_save
    b = b_save
    reszta = -1

    for n in range(0,100):
        a = a % b
        if reszta == a:
            if n < min_pos:
                min_pos = n
                min_i = i
        if i == n:
            reszta = a
        a *= 10

a = a_save
b = b_save
pos = 0
while pos < min_pos:
    if pos == min_i:
        print("(", end="")
    a = a % b
    a *= 10
    print(a//b, end="")
    pos += 1
print(")")