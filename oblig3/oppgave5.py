#Lag en metode som tar inn hvilke sporter folk liker, og sier hvor de kan holde paa med dem


steder = {
        "fotball" : "hemingbanen",
        "Squash" : "Lysaker squash",
        "ekstremprogrammering" : "ifi",
        "svømme" : "donus athletica",
        "tennis" : "slemdal eller no",
        "gaming" : "hjemme"
        }

def hvorsport():
    sporter = []
    #tar inn sporter helt til bruker inputter en tom string
    while True:
        a = input("Skriv en sport du liker. Trykk enter hvis du er ferdig")
        if a != "":
            sporter.append(a)
        else:
            break
    #itererer gjennom sportene dine og ser om det er i ordboken min
    for sport in sporter:
        if sport in steder:
            print("Du kan gjore %s paa %s" %(sport, steder[sport]))


hvorsport()
