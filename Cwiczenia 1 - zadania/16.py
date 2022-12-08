maxi = 0

for n in range(2,10001):
    nn = n
    counter = 0
    while nn != 1:
        nn = (nn%2)*(3*nn+1)+(1-nn%2)*nn/2
        counter += 1
    if counter > maxi:
        maxi = counter
        maxi_n = n

print(maxi_n)