

#Dette ser ut som fin kode, men jeg er litt usikker på hvordan printen takler int + string
#Plusse forskjellige typer mot hverandre kan ofte skape litt problemer, og naa har vi castet inputet
#over til et int. 

a = input("Tast inn et heltall! ")
b = int(a)
if b <10:
    print (b + "Hei!")
