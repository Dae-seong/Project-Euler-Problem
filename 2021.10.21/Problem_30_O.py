from math import *

N = 100000000

list = [0] * N
Sum = [0] * N

n = 1
Max = [0, 0]

for a in range (1, 1000) :

    for b in range (1, 1000) :

        for c in range (1, 1000) :

            if (pow (a, 2) + pow (b, 2) == pow (c, 2)) :

                list [n] = [a, b, c]

                n = n + 1

for i in range (1, n) :

    Sum [i] = list [i] [0] + list [i] [1] + list [i] [2]

for i in range (1, n) :

    if ( (Sum [i] <= 1000) and (Max [1] < Sum.count (i))) :
        
        Max = [i, Sum.count (i)]

print (Max)
