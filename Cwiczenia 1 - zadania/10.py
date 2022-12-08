for num in range(2,10**6):
    sum = 1
    i = 2
    while i**2 <= num:
        if num%i == 0:
            sum += i
            if i != num//i:
                sum += num//i
        i += 1
    if (num == sum):
        print (num)