

l = []
while True:
    a = int(input("Skriv et tall"))
    if a==0:
        break
    l.append(a)
##regner ut sum
minsum = 0
for i in l:
    print(i)
    minsum = minsum + i

print(minsum)

minste = None   #her lagres minste

#gaar gjennom listen og finner minste
for i in l:
    if minste == None:
        minste = i
    if i<minste:
        minste = i
print("minste er: " + str(minste))

storste = None #her lagres storste 


#Gaar gjennom listen og finner storste
for i in l:
    if storste == None:
        storste = i
    if i>storste:
        storste = i

print("storste  er: " + str(storste ))
    

