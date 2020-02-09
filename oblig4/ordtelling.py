
def antBok(etord):
    return len(etord)

def antOrd(setning):
    a = {}
    #for hvert ord i setningen
    for i in setning.split():
        #Hvis i ordbok, +1, hvis ikke, legg inn
        if i in a:
            a[i] = a[i] +1
        else:
            a[i] = 1

    return a


antBok("test")
print(antOrd("dette er en dette test"))
#Hvis i ordbok, +1, hvis ikke, legg inn


#her er hovedfunksjonen min
def main():
    tmp = input("Skriv en setning\n")
    bok = antOrd(tmp)
    #bruker funksjonene over.

    #itererer for hver nøkkel i ordboken
    for key in bok:
        print("Det er " + str(antBok(key)) + " bokstaver i " + key + ", og det nevnes ant: " + str(bok[key]))
    print("det er totalt ant ord: " + str(len(bok)))


main()
