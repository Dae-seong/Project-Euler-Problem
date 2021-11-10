from math import *

Prime = []

N = 100000

a = [False, False] + [True] * (N - 1)

Num_List = []

for i in range (2, N + 1):

    if a [i] :

        Prime.append (i)

        for j in range (2 * i, N + 1, i):

            a [j] = False

def Function (N) :

    if (int (sqrt (N)) == sqrt (N)) :

        return 

for i in range (2, N) :

    Num_List.append (i)

List = list (set (Num_List) - set (Prime))

Num_List = []

for i in List :

    for j in Prime :

        if (i > j) :

            if (((i - j) % 2) == 0) :

                N = int ((i - j) / 2)

                if (int (sqrt (N)) == sqrt (N)) :

                    if ((i % 2) != 0) :

                        Num_List.append (i)

                        break

Odd_List = []

for i in range (3, N, 2) :

    Odd_List.append (i)

print (list (set (Odd_List) - set (Num_List) - set (Prime)))