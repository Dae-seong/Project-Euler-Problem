from math import *

for a in range (100, 201) :

  for b in range (300, 400) :

    for c in range (400, 500) :

      if (pow (a, 2) + pow (b, 2) == pow (c, 2)) :

        if (a + b + c == 1000) :
          
          print (a, b, c)

          print (a*b*c)

          break