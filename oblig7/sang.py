class Sang:
    _tittel = None
    _artist = None



    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist


    def spill(self):
        #spill sang
        print("spiller sang ", self._tittel, " av: ", self._artist, ". ")
        return None

    def sjekkArtist(self, navn):
        for navniter in self._artist.split():
            for navn2 in navn.split():
                if navniter == navn2:
                    return True
        return False

    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel.lower():
            return True
        return False

    def sjekkArtistogTittel(self, artist, tittel):
        if self.sjekkArtist(artist) and self.sjekkTittel(tittel):
            return True
        return False




