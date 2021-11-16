from decimal import *

getcontext ().prec = 102

Sum = 0

for i in range (1, 100 + 1) :

    if ((Decimal (i) ** Decimal (1 / 2)) != int (Decimal (i) ** Decimal (1 / 2))) :

        List = []

        for j in str (Decimal (i) ** Decimal (1 / 2)) :

            if (str (j) != ".") :

                List.append (int (j))

        List.pop (-1)
        List.pop (-1)

        print (List)

        Sum = Sum + sum (List)

print (Sum)