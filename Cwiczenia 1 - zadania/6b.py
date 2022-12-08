a = 1
b = 10

while b-a > 0.0001:
    c = (a+b)/2
    d = c**c
    if d > 2020:
        b = c
    else:
        a = c
        
print(b)