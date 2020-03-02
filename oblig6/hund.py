class Hund:

    def __init__(self, alder, vekt, metthet=10):
        self.alder = alder
        self.vekt = vekt
        self.metthet = metthet

    

    def hentAlder(self):
        return self.alder




    def hentVekt(self):
        return self.vekt

    def spring(self):
        self.metthet-=1

        #Før eller etter? 
        if self.metthet<5:
            self.vekt-=1

    def spis(self, x):
        self.metthet+=x

        if self.metthet>7:
            self.vekt+=1





