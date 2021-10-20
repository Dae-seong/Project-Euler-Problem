from math import *

def Function (n) :

    S = 16 * pow (n, 3) / 3 + 10 * pow (n, 2) + (26 * n ) / 3 + 1

    return round (S)

N = 1001

n = (N - 1) / 2

print (Function (n))