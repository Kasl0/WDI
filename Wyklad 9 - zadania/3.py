#zmienne: x,y,z...
#stałe: 123, -32...
#operatory dwuargumentowe: ^ * / + -
#minus unarny: -
#nawiasy: ()

def oblicz(wyr):
    print(wyr)
    n = len(wyr)

    for i in range(n):
        if wyr[i] == "(":
            a = i
            while wyr[i] != ")":
                i += 1
            oblicz(wyr[a+1:i])
    
    for i in range(n):
        if wyr[i] == "^":
            pass

#wyrazenie = input()
wyrazenie = "(x+y)-(z*3)"

print(oblicz(wyrazenie))
#output: x y + z 3 * -


            
        
