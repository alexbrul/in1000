
#definener adder
def adder(tall1, tall2):
    return tall1 + tall2
#sender tallene inn i adder og printer det ut med tekst til
print("5 + 5 er lik: " + str(adder(5,5)))
print("1 + 2 er lik: " + str(adder(1,2)))

tekst = input("Skriv en streng")
bokstav = input("Skriv en bokstav")

def tellForekomst(mintekst, minbokstav):
    counter = 0 #teller antall bokstaver

    #for alle bokstavene i teksten, se om bokstaven er lik teksten.
    for i in mintekst:
        if i == minbokstav:
            counter= counter+1 #hvis den er det. ta plus 1

    return counter
#Skjonnte ikke helt hva dere mente
print(tellForekomst(tekst, bokstav))
print(tellForekomst(input("Skriv en streng"), input("Skriv en bokstav")))










