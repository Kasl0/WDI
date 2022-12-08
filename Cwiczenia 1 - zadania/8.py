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
    
num = int(input("num="))
print(prime(num))