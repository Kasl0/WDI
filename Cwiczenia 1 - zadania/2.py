def fib(a_start, b_start):
    a = a_start
    b = b_start
    while a <= 2022:
        if a == 2022:
            print(a_start, b_start)
            exit()
        a, b = a + b, a

for sum in range(2, 1000):
    for a in range (1, sum):
        fib(a, sum-a)