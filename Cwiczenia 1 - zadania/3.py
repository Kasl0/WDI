def fib():
    fib_list = [1, 1]
    for i in range(2,20):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

list = fib()
sum = int(input("sum="))
s = 0
start_point = 0

for value in list:
    s += value
    while s > sum:
        s -= list[start_point]
        start_point += 1
    if s == sum:
        print("yes")
        exit()
print("no")


