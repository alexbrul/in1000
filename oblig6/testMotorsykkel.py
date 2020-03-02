import sys
from motorsykkel import Motorsykkel




def hovedprogram():

    a = Motorsykkel("honda", "ek291", 100)
    b = Motorsykkel("tesla", "ek299", 219)
    c = Motorsykkel("honda", "ek111111", 999)
    print(a.hentKilometerstand())
    a.kjor(100)
    print(a.hentKilometerstand())

    a.skrivUt()
    b.skrivUt()
    c.skrivUt()
    print("kjorer 10 paa siste")
    c.kjor(10)
    c.skrivUt()

hovedprogram()

