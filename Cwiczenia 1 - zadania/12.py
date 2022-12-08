a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

if a<b:
    min = a
else:
    min = b
if c<min:
    min = c

nwd = 1
d = 2
while d <= min:
    if a%d == 0 and b%d == 0 and c%d == 0:
        a = a//d
        b = b//d
        c = c//d
        min = min//d
        nwd *= d
    else:
        d += 1

print(nwd)