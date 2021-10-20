N = [0] * 10000000

n = [0] * 10000000

Start = 0

Max = 0

Count = 0

for i in range (1, 1000000 + 1) :

    N [i] = i

    k = 0

    for j in range (1, 10000) :

        if ((N [i] % 2) == 0) :

            N [i] = N [i] / 2

            k = k + 1

        if (N [i] == 1) :

            break

        if ((N [i] % 2) != 0) :

            N [i] = 3 * N [i] + 1

            k = k + 1

    n [i] = k

    if (n [i] > Max) :

        Max = n [i]

        Count = i

print (Max, Count)