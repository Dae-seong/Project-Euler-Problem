from math import *

list = [0] * 100000

for i in range (1, 10000) :

    list [i] = int (i * (3*i - 1) / 2)

for i in range (1, 10000) :

    for j in range (i, 10000) :

        for k in range (i // 2, j) :

            if (list [j] - list [i] == list [k]) :

                for l in range (j, 2 * j) :

                    if (list [i] + list [j] == list [l]) :

                        print (abs (list [i] - list [j]))

                        break