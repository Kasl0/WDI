a = int(input("a="))
b = int(input("b="))
n = int(input("n="))

iloraz = str(a/b)
poz = 0

while iloraz[poz] != ".":
    print(iloraz[poz], end="")
    poz += 1
    
for i in range(poz, poz+n+1):
    if i < len(iloraz):
        print(iloraz[i], end="")
    else:
        print(iloraz[len(iloraz)-1], end="")
