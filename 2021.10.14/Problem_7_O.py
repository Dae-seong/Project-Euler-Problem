from math import *

Prime_ = []

n = 105000

b = 0

a = [False, False] + [True] * (n-1)

for i in range (2, n+1):

  if a [i]:

    Prime_.append (i)

    b = b + 1

    for j in range (2 * i, n + 1, i):

        a [j] = False

print (Prime_[10000])