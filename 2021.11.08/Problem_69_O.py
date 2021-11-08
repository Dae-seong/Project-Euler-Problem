from fractions import *
from math import *

Prime = []

N = 1000000

a = [False, False] + [True] * (int (sqrt (N))-1)

for i in range (2, int (sqrt (N))+1):

  if a [i]:

    Prime.append (i)

    for j in range (2 * i, int (sqrt (N)), i):

        a [j] = False

Max = [0, 0]

for i in range (2, 1000000 + 1) :

    List = []

    N = 1
    
    for j in range (len (Prime)) :

        if ((i % Prime [j]) == 0) :

            List.append (Prime [j])

    for j in List :

        N = N * (1 - Fraction (1, j))

    if ((1 / N) > Max [0]) :

        Max = [(1 / N), i]

print (Max)