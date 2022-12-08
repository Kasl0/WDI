a = int(input("a="))
b = int(input("b="))
n = int(input("n="))
nn = n

print(a//b, end=".")

#1
while n>0:
    a *= 10
    print((a//b)%10, end="")
    n -= 1

#2
"""
while n>0:
    a = a % b
    a *= 10
    print(a//b,end="")
    n -= 1
"""
