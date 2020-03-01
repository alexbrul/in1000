

#Hver person har sine egne mål. 
#Alle personer er lagret i navn.txt


personer = []

def lesInn(filnavn):
     
    with open(filnavn, "r") as infile:
        dictt = {}
        for line in infile.readlines():
            line = line.split()
            dictt[line[0]] = line[1] 

    personer.append([filnavn[:len(filnavn)-4], dictt])

def printPerson(navn):
    if navn == "alle":
        for i in personer:
            print(i[0], "  :   ", i[1])
        return
    for i in personer:
        if i[0] == navn:
            print(i[0], " : " , i[1])

a = "hei"
while(a!= ""):
    a = input("Skriv et filnavn for å legge til person,, eller p for å printe personer, rller en tom streng for å avslutte! ")
    if a != "p":
        lesInn(a)
    elif a == "p":
        a = input("Skriv navn, eller 'a' for alle ")
        if a == "a":
            printPerson("alle")
        else: 
            printPerson(a)
    elif a == "":
        break

print(personer)




