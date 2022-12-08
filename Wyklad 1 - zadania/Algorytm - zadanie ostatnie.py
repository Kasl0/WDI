N = int(input("> "))
max_iloczyn = 1
while True:
    if N>4 or N==3:
        max_iloczyn *= 3
        N -= 3
    elif N==4:
        max_iloczyn *= 4
        N -= 4
    elif N==2:
        max_iloczyn *= 2
        N -= 2
    if N < 2:
        break

print(max_iloczyn)