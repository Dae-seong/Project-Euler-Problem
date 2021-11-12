Prime = []

N = 1000000

a = [False, False] + [True] * (N - 1)

for i in range (2, N + 1):

    if a [i] :

        Prime.append (i)

        for j in range (2 * i, N + 1, i):

            a [j] = False

Max = [0, 0]

for i in range (0, len (Prime)):

    Sum = Prime [i]

    Count = 1

    for j in range (i + 1, len (Prime)) :

        Sum = Sum + Prime [j]

        Count = Count + 1

        if (Sum > 1000000) :

            break

        if (Count > Max [1]) :

            if Sum in Prime :

                Max = [Sum, Count]

                print (Sum, Count)

print (Max)