N = int(input("N="))

suma = 0
iloczyn = 1

iloczyn_trojek = 1
iloczyn_piatek = 1

while iloczyn <= N:
    while iloczyn <= N:
        while iloczyn <= N:
            suma += 1
            iloczyn *= 2
        iloczyn_trojek *= 3
        iloczyn = iloczyn_trojek * iloczyn_piatek
    iloczyn_piatek *= 5
    iloczyn_trojek = 1
    iloczyn = iloczyn_trojek * iloczyn_piatek

print(suma)
