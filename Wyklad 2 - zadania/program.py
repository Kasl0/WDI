def sum_p(n):
    n = str(n)
    p = len(n)
    sum = 0
    for i in range(p):
        sum += int(n[i])**p
    if sum == int(n):
        return sum
    else:
        return 0

def prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i**2 <= n:
        if n%i == 0:
            return False
        i += 2
    return True

for n in range(0,10**9):
    if sum_p(n) == 0:
        continue
    break_flag = False
    if n == 2 or n == 3:
        print(sum_p(n))
    if n < 2 or n%2 == 0 or n%3 == 0:
        continue
    i = 5
    while i**2 <= n:
        if n%i == 0:
            break_flag = True
            break
        i += 2
        if n%i == 0:
            break_flag = True
            break
        i += 4
    if break_flag == False:
        print(sum_p(n))