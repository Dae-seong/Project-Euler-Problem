def Sum (N) :

    if ((N != 1) and (N != 89)) :

        return (Sum (sum ([(int (a) ** 2) for a in str (N)])))

    if ((N == 1) or (N == 89)) :

        return (N)

Count = 0

for i in range (1, 10000000) :

    if (Sum (i) == 89) :

        Count = Count + 1

print (Count)