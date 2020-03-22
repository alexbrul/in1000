from sang import Sang
#importerer den andre klassen

class Spilleliste:
    #konstruktør
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):

        #med fil, for linje i filen, splitter opp og fikser. ?strip? fjerner mellomrom?
        with open(filnavn, "r") as infile:
            for line in infile:
                line = line.strip().split(';')
                newsang = Sang(line[0], line[1])
                self._sanger.append(newsang)

    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        self._sanger.remove(sang)

    def spillSang(self, sang):
        sang.spill()

    def spillAlle(self):
        for i in self._sanger:
            i.spill()

    def finnSang(self, tittel):
        for i in self._sanger:
            if i.sjekkTittel(tittel):
                return i
        return None

    def hentArtistUtvalg(self, artistnavn):
        #lager en liste til å lagre innholdet
        tmp = []
        #for alle sanger i spillelisten, hvis artisten stemmer, så legg til i tmp
        for i in self._sanger:
            if i.sjekkArtist(artistnavn):
                tmp.append(i)

        return tmp


