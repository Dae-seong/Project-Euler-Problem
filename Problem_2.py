from math import *

e_ = [0] * 50000000

e_[1] = 1
e_[2] = 1

for i in range (3, 10002) :

    e_[i] = e_[i-1] + e_[i-2]

print ("%d" % (e_[3]))
