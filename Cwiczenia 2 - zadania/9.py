k = float(input("k="))
dokladnosc = k / 100
i = 1
pole = 0

while i < k:
    pole += dokladnosc / (i + (dokladnosc/2))
    i += dokladnosc
    
print(pole)
