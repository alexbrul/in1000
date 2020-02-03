varebok = {
        "melk": 14.90,
        "brød": 24.90,
        "yoghurt": 12.90,
        "pizza": 39.90
        }

print(varebok)

for i in range(2):
    vare = input("Skriv vare \n")
    pris = input("Skriv pris \n")
    varebok[vare] = float(pris)

print(varebok)
