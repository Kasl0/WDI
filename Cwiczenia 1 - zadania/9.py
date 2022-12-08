num = int(input("num="))

i = 1
while i**2 <= num:
    if num%i == 0:
        print(i)
        if i != num//i:
            print(num//i)
    i += 1