import sys

from spillebrett import Spillebrett

def Main():
    a = input("Skriv inn antall rader og kolonner med et mellomrom i mellom. typ 10 10 \n").split()
    r = Spillebrett(int(a[0]), int(a[1]))

    r.tegnBrett()
    inp = input("Trykk enter for å rulle, eller q for å avslutte, eller tall n for å rulle n ganger\n")

    while(inp!="q"):
        if inp == "":
            r._oppdatering()
        else:
            for i in range(int(inp)):
                r._oppdatering()
        print("Generasjon: ", r.generasjon)
        print("AntLevende: " + str(r.finnAntallLevende()))

        r.tegnBrett()
        inp = input("Trykk enter for å rulle, eller q for å avslutte, eller tall n for å rulle n ganger\n")

Main()
