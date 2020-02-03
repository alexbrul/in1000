
def nyBillett(alder):
    billettpris = 0
    # ok, s√ tilfellet beskrevet i obligen hadde ikke fungert helt fordi alle over
    #63 er ogsaa over 17. Fra f√rste test vet vi at alle de osm kom videre er over 17.
    #S√ hvis man ikke er yngre enn 63 saa betaler man vanlig billett
    if(alder <=17):
        billettpris = 30
    elif alder < 63:
        billettpris = 50
    else:
        billettpris = 35
    print("Billettprisen din er %.2f kr" %billettpris)

#Her bare kjorer jeg prosedyren 4 ganger med nytt input hver gang.
for i in range(4):
    nyBillett(int(input("Hvor gammel er du?\n")))


#6
#Hvis brukeren skriver en string vil det bli error i konverteringen til int. 
#Alle tall under 0 gir helder ikke mening. 


