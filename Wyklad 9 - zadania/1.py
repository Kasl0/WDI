def f(a, b):
    if a == 0:
        return b + 1
    if a > 0 and b == 0:
        return f(a-1, 1)
    if a > 0 and b > 0:
        return f(a-1, f(a, b-1))
    
a = int(input("a="))
b = int(input("b="))
print(f(a, b))