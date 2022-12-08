samogloski = 'a', 'e', 'i', 'o', 'u', 'y'

def wyraz(s1, s2):
    ile = 0
    suma = 0
    for litera in s1:
        suma += ord(litera)
        if litera in samogloski:
            ile += 1
    
    ret = zbuduj(s2, suma, ile)
    if ret:
        return (True, ret)
    else:
        return False

def zbuduj(litery, suma, ile, wyr=""):
    if suma == 0 and ile == 0:
        return wyr
    if suma <= 0 or ile < 0:
        return False

    for litera in litery:
        if litera in samogloski:
            ret = zbuduj(litery, suma-ord(litera), ile-1, wyr+litera)
            if ret:
                return ret
        else:
            ret = zbuduj(litery, suma-ord(litera), ile, wyr+litera)
            if ret:
                return ret
    return False

print(wyraz("ula","exe"))