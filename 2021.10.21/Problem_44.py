from math import *

"""list = [0] * 100000
Sum = [0] * 100000
Sub = [0] * 100000

for i in range (1, 10000) :

    list [i] = int (i * (3*i - 1) / 2)

    Sum [i] = [0] * 100000
    Sub [i] = [0] * 100000

for i in range (1, 1000) :

    for j in range (1, 1000) :

        Sum [i] [j] = [list [i] + list [j]]
        Sub [i] [j] = [abs (list [i] - list [j])]

for i in range (1, 1000) :

    for j in range (1, 1000) :

        for k in range (1, 10000) :

            for l in range (1, 10000) :

                if ((Sum [i] [j] == list [k]) and (Sub [i] [j] == list [l])) :

                    print (Sub [i] [j])
                    
                    break"""

for a in range (1, 10000) :

    for b in range (a, 10000) :

        for c in range (1, 10000) :

            if ((b + a != c) and ((pow (b, 2) + pow (a, 2) - pow (c, 2)) / (b + a - c) == 1/3)) :

                for d in range (1, 10000) :

                    if ((b - a != d) and ((pow (b, 2) - pow (a, 2) - pow (d, 2)) / (b - a - d) == 1/3)) :

                        print (a, b, c, d)

                        break