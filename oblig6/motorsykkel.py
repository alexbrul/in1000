class Motorsykkel:


    def __init__(self, merke, regnr, km):
        self.merke = merke
        self.regnr = regnr
        self.km = km





    def kjor(self, km):
        self.km += km

    def hentKilometerstand(self):
        return self.km

    def skrivUt(self):
        print(self.merke, self.regnr, self.km)

