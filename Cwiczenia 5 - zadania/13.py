def podzial(n, skladniki=()):
    if skladniki:
        print(skladniki+(n,))
            
    for i in range(1,n):
        if not skladniki or skladniki[-1] <= i:
            if i <= n-i:
                podzial(n-i, skladniki+(i,))

n = int(input("n="))
podzial(n)