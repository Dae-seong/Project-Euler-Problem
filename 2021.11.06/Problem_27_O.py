from math import *

Prime = []

N = 10000

a = [False, False] + [True] * (N - 1)

Max = 0

for i in range (2, N + 1):

    if a [i] :

        Prime.append (i)

        for j in range (2 * i, N + 1, i):

            a [j] = False

for a in range (-1000, 1000) :

    for b in range (-1000, 1000) :

        Count = 0

        for n in range (0, 80) :

            if (n**2 + a*n + b) in Prime :

                Count = Count + 1

            if (n**2 + a*n + b) not in Prime :

                break

        if (Count > Max) :

            Max = Count

            list = [a, b, Count, a * b]

print (list)