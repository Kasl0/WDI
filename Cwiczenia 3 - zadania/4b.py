"""s = 1
w = 1
i = 1

while w > 0:
    s = s + w
    i += 1
    w = w/i

print(s)"""

n = int(input("n="))

s = [0 for _ in range(n+1)]
s[0] = 1
w = [0 for _ in range(n+1)]
w[0] = 1

i = 1
while max(w) > 0:
    p = 0
    for j in range(n, -1, -1):
        p = s[j] + w[j] + p
        s[j] = p % 10
        p = p//10
    i += 1

    r = 0
    for j in range(0, n+1):
        r = r * 10 + w[j]
        w[j] = r // i
        r = r % i

print(s[0], end="")
print(".", end="")
for i in range(1, n+1):
    print(s[i], end="")