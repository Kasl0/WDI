from math import sqrt
result = 1
last = sqrt(0.5)

for n in range(1,10**6):
    result *= last
    last = sqrt(0.5 + 0.5 * last)
    
print(2/result)