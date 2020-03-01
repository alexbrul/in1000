

temperaturer = []


with open("temperatur.txt", "r") as infile:
    #leser alle linjene, og itererer gjennom dem etterpå. 
    for line in infile.readlines():
        temperaturer.append(int(line)) ##legger til liste


print(temperaturer)  # Ser at alle det har funket.

def gjennomsnitt(temperaturer):
    #Legger alle tallene til counter for å få sum, for deretter å dele på antall

    counter = 0
    for item in temperaturer:
        counter+= item

    return counter/len(temperaturer)

print("Gjennomsnittet av temperaturene er :" , gjennomsnitt(temperaturer))





