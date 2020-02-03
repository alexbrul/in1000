#program som lager en liste og legger til ting. Læring av lister generelt
a = [1, 2, 3]
#legger til 4
a.append(4)
#Liste for navn
navn = []
#Tar inn 3 navn
for i in range(3):
    navn.append(input("Skriv et navn\n"))
#Sjekker om navnet mitt er i listen
if "Alexander" in navn:
    print("Du husket meg!")
else:
    print("Glemte du meg?")
#holder verdier
summen = 0
produktet = 1

#regner ut summen og produktet
for i in a:
    summen = summen + i
    produktet = produktet*i
b = [summen, produktet]
#plusser listene
c = a + b
print(c)

#fjerner elementer ved hjelp av slicing. 
del c[-2:]
print(c)



