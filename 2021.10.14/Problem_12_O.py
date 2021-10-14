from math import *

n = 15000
Num_Sum_ = [0] * n

for i in range (1, n) :

    for j in range (1, i + 1) :

        Num_Sum_[i] = Num_Sum_[i] + j

for i in range (1, n) :

    Counting = 0

    for j in range (1, 1000000) :

        if (Num_Sum_[i]%j == 0) :

            Counting = Counting + 1

            if (Counting == 500) :

                break

    if (Counting == 500) :

        print (Num_Sum_[i])

        break
