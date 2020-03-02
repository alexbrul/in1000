from hund import Hund

def hovedprogram():

    ralf = Hund(1, 15)
    for i in range(2):
        ralf.spring()
        print(ralf.hentVekt())
        ralf.spis(1)
        print(ralf.hentVekt())
   
hovedprogram()


