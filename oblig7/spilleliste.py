from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):

        with open(filnavn, "-r") as infile:
            for line in infile:
                line = linje.strip().split(';')
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
            if sjekkTittel(tittel):
                return i
        return None

    def hentArtistUtvalg(self, artistnavn):
        tmp = []

        for i in self._sanger:
            if i.sjekkArtist(artistnavn):
                tmp.add(i)


