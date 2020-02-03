
#Lager matplanordboken
matplaner = {
        "Preben": ["egg", "nutrilett", "biff"],
        "Leif-Vidar": ["vann", "is", "nudler"]
        }

#En metode som kalles for sjekke  ordboken paa en lett mate 
def finnMat():
    #Tar inn input og haandterer det
    a = input("Skriv navnet til personen du vil ha maaltidene til")
    #hvis personen er i ordboken min
    if a in matplaner:
        print(matplaner[a])

    else:
        print("Dette navnet er ikke registrert")

finnMat()


#3
#a) For alle in1000 studentene ville jeg brukt en liste. De er fint aa ha sortert og man kan raskt iterere gjennom
#b) for brukernavn og poeng er det viktig aa kunne slaa opp raskt. Dicts bruker hashing, og ville derfor brukt en slik en.
#c) Det er ikke mange vinnere i lotto, og disse er ogsa kult aa lagre sortert. 
#d) hvis man skal lagre mat folk er allergisk mot kunne man brukt en mengde for aa hindre
#duplikater. Men siden storrelsene er saa smaa saa betyr det egentlig ikke saa stor rolle.







