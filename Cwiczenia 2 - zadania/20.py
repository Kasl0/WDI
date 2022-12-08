a = int(input("a="))
b = int(input("b="))

for podstawa in range(2,17):
    flag = False
    a_temp = a
    while flag == False and a_temp > 0:
        cyfra = a_temp % podstawa
        a_temp //= podstawa

        b_temp = b
        while b_temp > 0:
            if b_temp % podstawa == cyfra:
                flag = True
                break
            b_temp //= podstawa

    if flag == False:
        print(podstawa)
        exit()
