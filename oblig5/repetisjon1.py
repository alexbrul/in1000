


mineOrd = []

def slaaSammen(a, b):
    return a + b


def skrivUt(liste):
    for i in liste:
        print(i)
inp = ''
while(inp!= 's'):
    inp = input("Skriv enten i(nsert), u(utskriv) eller s(top)")
    if inp == 'i':
        w1 = input("Skriv ord 1: ")
        w2 = input("Skriv ord 2: ")
        mineOrd.append(slaaSammen(w1,w2))
    elif inp == 'u':
        skrivUt(mineOrd)

