from math import *

e_ = [0] * 50000000

Sum = 0

e_[1] = 1
e_[2] = 2

for i in range (3, 100) :

    e_[i] = e_[i-1] + e_[i-2]

for i in range (1, 100) :

    if (e_[3*i - 1] > 4000000) :

        break

    Sum = Sum + e_[3*i - 1]

print (Sum)
