#Lag et helseprogram som kan hjelpe studenter med mat, trening, og helse.
#Tar inn input fra bruker
f = int(input("Hvor mange dager i uken spiser du fisk? \n"))

#bruker en if stmt for aa sjekke mengden til f
if f>6:
    print("Du er gal")

#Hvis f ikke er hÃyere enn 6 skal den prÃve dette
elif f >= 3:
    print("Du er veldig flink")
#Hvis ingen av de andre if elif elif elif slÃr ut skal den kjore else. 
else:
    print("Du burde spise fisk oftere")




t = int(input("Hvor mange dager i uken trener du? \n"))
if t>6:
    print("Du er gal")
elif t >= 3:
    print("Du er veldig flink")
else:
    print("Det er kanskje lurt aa begynne med litt trening")



f = int(input("Hvor mange dager i uken er du pÃ¥skolen \n"))
if f>=6:
    print("Du er gal")
elif f >= 5:
    print("Du er veldig flink")
else:
    print("Du leser sikkert bra hjemme")
