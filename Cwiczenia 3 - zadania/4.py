from math import factorial

N = int(input("N="))
e = 0

for i in range(0, 100):
    e += 1/factorial(i)

print(int(e), end=".")
while N > 0:
    e *= 10
    print(int(e)%10, end="")
    N -= 1