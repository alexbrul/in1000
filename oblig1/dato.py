d1 = input("Dag 1")
m1 = input("Maaned1")

d2 = input("Dag 2")
m2 = input("Maaned2")

if int(m1)< int(m2):
    print("Riktig rekkefolge")
elif int(m1) > int(m2):
    print("Feil rekkefolge")
elif int(m1) == int(m2):
    if int(d1) == int(d2):
        print("Samme dato")
    elif int(d1)< int(d2):
        print("Riktig rekkefolge")
    else:
        print("Feil rekkefolge")
