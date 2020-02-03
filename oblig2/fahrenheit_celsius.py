
#tar inn input fra bruker.
fhr = int(input("Skriv temperatur i fahrenheit\n"))

#printer input
print(fhr)

#Sier at celsius er lik funksjonen av fhrnheit
celsius = (fhr - 32) * 5.0/9.0

#printer celsius med noe tekst for Ã¥ gjÃre det mer forstÃelig.
print("Temperaturen i celsius er: %f" %celsius)
