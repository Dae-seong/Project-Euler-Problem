from math import *

abc = 0

for a in range (200, 300) :

    for b in range (300, 400) :

        for c in range (400, 500) :

            if (pow (a, 2) + pow (b, 2) == pow (c, 2)) :

                if (a + b + c == 1000) :

                    abc = a * b * c

print (abc)