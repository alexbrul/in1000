class Sang:
    _tittel = None
    _artist = None



    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist


    def spill():
        #spill sang
        print("spiller sang ", _tittel, " av: ", _artist, ". ")
        return None

    def sjekkArtist(navn):
        for navniter in self.artist.split():
            for navn2 in navn.split():
                if navniter == navn:
                    return True
        return False

    def sjekkTittel(tittel):
        if tittel.lower() == _tittel.lower():
            return True
        return False

    def sjekkArtistOgTittel(artist, tittel):
        if sjekkArtist(artist) and sjekkTittel(tittel):
            return True
        return False




