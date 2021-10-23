from math import *

List = []

for i in range (3, 50000) :

    list = []

    Sum = 0

    N = 0

    for j in str (i) :

        list.append (int (j))

        N = N + 1

    for j in range (0, N) :

        Sum = Sum + factorial (list [j])

    if (i == Sum) :

        List.append (i)

print (List)