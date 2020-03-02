



def innlesing(filnavn):
    guleSider = {}
    
    with open(filnavn, "r") as infile:
        for line in infile.readlines():
            line = line.split()

            guleSider[line[0]] = int(line[1])

    return guleSider


def maanedensSalgsPerson(ob):
    print(max(ob, key=ob.get), ob[max(ob, key=ob.get)])


def totalAntallSalg(ob):
    counter = 0
    for i in ob:
        counter+= ob[i]
    return counter


def gjennomsnittSalg(ob):
    return totalAntallSalg(ob)/len(ob)


def hovedprogram(filnavn):
    a = innlesing(filnavn)
    print("Filnavnet er", filnavn)
    print("Maanedens Salgs Person:") 
    maanedensSalgsPerson(a)
    print("Total antall salg:", totalAntallSalg(a))
    print("GjennomsnittSalg: ", gjennomsnittSalg(a))
    print("Antall personer lest inn:", len(a))

hovedprogram("salgsliste.txt")







