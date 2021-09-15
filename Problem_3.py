from math import *

Prime_ = []
Prime_Factor = 0
Prime_Factor_ = [0] * 10

n = 600851475143

b = 0

a = [False, False] + [True] * (int (sqrt (n))-1)

for i in range (2, int (sqrt (n))+1):

  if a [i]:

    Prime_.append (i)

    b = b + 1

    for j in range (2 * i, int (sqrt (n)), i):

        a [j] = False

for i in range (0, b) :

    if (n%Prime_[i]==0) :

      Prime_Factor_[Prime_Factor] = Prime_[i]

      Prime_Factor = Prime_Factor + 1

print (Prime_Factor_)