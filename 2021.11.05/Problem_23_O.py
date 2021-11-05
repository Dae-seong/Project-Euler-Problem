from math import *

N = 28123

Sum = [0] * N
List = []
Total = []

for i in range (1, N) :

    for j in range (1, i - 1) :

        if (i % j == 0) :

            Sum [i] = Sum [i] + j

    if (Sum [i] > i) :

        List.append (i)

for i in range (0, len (List)) :

    if (List [i] < 28123) :

        for j in range (0, len (List)) :

            if (List [j] < 28123) :

                if ((List [i] + List [j]) > 28123) :
                    
                    break
                
                if ((List [i] + List [j]) < 28123) :

                    Total.append (List [i] + List [j])

Total = list (set (Total))

print (395437503 - sum (Total))