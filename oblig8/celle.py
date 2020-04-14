class Celle:
    levende = False

    #konstruktør
    def __init__(self): 
        self.levende = False


    def settDoed(self):
        self.levende = False

    def settLevende(self):
        self.levende = True

    def erLevende(self):
        return self.levende

    def __str__(self):
        if self.levende:
            return "O"
        return "."



