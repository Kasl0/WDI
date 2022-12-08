a = 1
b = 10

def f(n):
    return n**n - 2020

while b-a > 0.0001:
    x = (a + b)/2
    if f(x) == 0:
        break
    if f(a)*f(x) < 0:
        b = x
    else:
        a = x

print(x)

    