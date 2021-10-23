from math import *

k = 0

for n in range (1, 100 + 1) :

    for r in range (1, n + 1) :

        if ((factorial (n) / (factorial (r) * factorial (n - r))) > 1000000) :

            k = k + 1

print (k)