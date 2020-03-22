class Sang:

    #konstruktør
    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist


    def spill(self):
        #spill sang
        print("spiller sang ", self._tittel, " av: ", self._artist, ". ")

    def sjekkArtist(self, navn):
        #for hvert navn i artisten, se om et av navnene vi får inn stemmer.
        for navniter in self._artist.split():
            for navn2 in navn.split():
                if navniter == navn2:
                    return True
        return False

    def sjekkTittel(self, tittel):
        #bruker .lower() for å gjøre begge om til lowercase
        if tittel.lower() == self._tittel.lower():
            return True
        return False

    def sjekkArtistogTittel(self, artist, tittel):
        #bare kaller paa de andre metodene.
        if self.sjekkArtist(artist) and self.sjekkTittel(tittel):
            return True
        return False




