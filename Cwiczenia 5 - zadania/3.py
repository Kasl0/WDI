from random import randint

def ruch(tablica, x, y, koszt):
    koszt += tablica[x][y]
    if x==7:
        return koszt
    mini = ruch(tablica, x+1, y, koszt)
    if y-1 >= 0:
        mini = min(mini, ruch(tablica, x+1, y-1, koszt))
    if y+1 <= 7:
        mini = min(mini, ruch(tablica, x+1, y+1, koszt))
    return mini

T = [[randint(1,10) for _ in range(8)] for _ in range(8)]
for i in range(len(T)):
    print(T[i])

k = int(input("k="))
print(ruch(T, 0, k, 0))