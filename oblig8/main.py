import sys

from spillebrett import Spillebrett

a = Spillebrett(20, 20)

a.tegnBrett()
for i in range(15):
    a._oppdatering()
    a.tegnBrett()

