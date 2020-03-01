


def addisjon(x, y):
    return x + y

print(addisjon(2,2))

def substraksjon(x, y):
    return x - y
def divisjon(x, y):
    return x / y 


#tester funskjoner.
assert substraksjon(2, 2) == 0
assert substraksjon(2, 4) == -2
assert substraksjon(-2, -2) == 0
assert divisjon(2, 2) == 1
assert divisjon(8, 4) == 2
assert divisjon(-2, -2) == 1
assert addisjon(2, 2) == 4
assert addisjon(2, 4) == 6
assert addisjon(-2, -2) == -4



def tommerTilCm(antallTommer):
    assert antallTommer>=0
    return antallTommer*2.54

assert tommerTilCm(1) == 2.54 

def skrivBeregninger():
    x = float(input("Skriv inn tall 1: "))
    y = float(input("Skriv inn tall 2: "))
    print("Resultatet av summering: " + str(addisjon(x,y)))
    print("Resultatet av substraksjon: " + str(substraksjon(x,y)))
    print("Resultatet av divisjon: " + str(divisjon(x,y)))

    print(str(tommerTilCm(float(input("skriv et tall som skal konverteres fra tommer til cm: ")))))

skrivBeregninger()






