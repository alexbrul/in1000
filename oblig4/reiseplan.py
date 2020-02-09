



steder = []

for i in range(5):
    steder.append(input("Skriv et reisemål"))

klesplagg = []
avreisedatoer  = []

for i in range(5):
    klesplagg.append(input("Skriv et klesplagg"))
    avreisedatoer.append(input("Skriv en avreisedato"))

reiseplan = [steder, klesplagg, avreisedatoer]

for i in reiseplan:
    print(i)


i1 = int(input("Skriv et tall mellom 1 og 3")) - 1
i2 = int(input("Skriv et tall mellom en og 5")) -1
if i1 < len(steder) and i2 < int(len(klesplagg)):
    print(reiseplan[i1][i2])
else:
    print("Ugylding input")

