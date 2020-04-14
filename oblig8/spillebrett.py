from celle import Celle
import random


class Spillebrett:
    _rader = None
    _kolonner = None
    generasjon = 0
    rutenett = None
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._generer()

    def _generer(self):
        self.rutenett = []
        for i in range(self._rader):
            self.rutenett.append([])
        for i in self.rutenett:
            for k in range(self._kolonner):
                tmp = Celle()
                if random.randint(0,3) == 0:
                    tmp.settLevende()
                i.append(tmp)


    def tegnBrett(self):
        print("\n \n")
        for i in self.rutenett:
            p = ""
            for a in i:
                p = p + a.__str__()
            print(p)


    def finnNabo(self, rad, kolonne):
        r = self.rutenett
        a = []
        #opp
        if rad > 0:
            a.append(r[rad-1][kolonne])
        #venstre
        if kolonne >0: 
            a.append(r[rad][kolonne-1])
        #høyre, mindre enn og kolonner-1 blir 2, sså forst til kordinat, såå en ned
        if kolonne<self._kolonner-1:
            a.append(r[rad][kolonne+1])
        #ned 
        if rad<self._rader-1:
            a.append(r[rad+1][kolonne])
        #oppvenstre
        if (rad>0) and (kolonne >0):
            a.append(r[rad-1][kolonne-1])
        #opphøyre
        if (rad>0) and (kolonne<self._kolonner-1):
            a.append(r[rad-1][kolonne+1])
        #nedvenstre
        if (rad<self._rader-1) and (kolonne >0):
            a.append(r[rad+1][kolonne-1])
        #nedhoyre
        if (rad<self._rader-1) and (kolonne < self._kolonner-1):
            a.append(r[rad+1][kolonne+1])
            
        return a

    def _oppdatering(self):
        # levende -> 1 nabo = dø, 2-3 = bli levende, 4 = dø
        # død -> if 3 = leve
        bliLevende = []
        slaktet = []
        icounter = 0
        kcounter = 0

        for i in range(len(self.rutenett)):
            for k in range(len(self.rutenett[i])):
                naboer = self.finnNabo(i, k)
                levnab = 0
                for q in naboer:
                    if q.erLevende():
                        levnab = levnab+1


                if self.rutenett[i][k].erLevende():
                    if levnab <2 or levnab == 4:
                        slaktet.append(self.rutenett[i][k])
                else:
                    if levnab == 3:
                        bliLevende.append(self.rutenett[i][k])

        for i in bliLevende:
            i.settLevende()
        for i in slaktet:
            i.settDoed()





        




