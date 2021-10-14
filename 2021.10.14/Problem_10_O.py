from math import *

Sum = 0
n = 2000000
b = 0

Prime_ = []
a = [False, False] + [True] * (n-1)

for i in range (2, n+1):

  if a [i]:

    Prime_.append (i)

    b = b + 1

    for j in range (2 * i, n + 1, i):

        a [j] = False
        
for i in range (0, b) :

    Sum = Sum + Prime_[i]

print (Sum)