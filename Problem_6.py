from math import *

sum_1 = 0
sum_2 = 0
n=10

for i in range (1, n+1) :

  sum_1 = sum_1 + i

print (pow (sum_1, 2))

for i in range (1, n+1) :

  sum_2 = sum_2 + pow (i, 2)

print (sum_2)

print (pow (sum_1, 2) - sum_2)