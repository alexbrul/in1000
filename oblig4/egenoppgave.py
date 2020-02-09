import random

#Her er en oppgave for å finne ut hva barnet ditt skal hete.
#Skriv de navnene du vurderer, så velger den et upartisk navn

def minoppgave():
    a= []
    for i in range(10):
        a.append(input("skriv et navn"))

    random.shuffle(a)
    return str("Barnet ditt skal hete: " + a[0])

print(minoppgave())


