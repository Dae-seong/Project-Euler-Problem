from fractions import *

N = 0

Count = 0

for i in range (1000, 0, -1) :

    N = Fraction (1 / (2 + N))

    if (len (str ((1 + N).numerator)) > len (str ((1 + N).denominator))) :

        Count = Count + 1

print (Count)