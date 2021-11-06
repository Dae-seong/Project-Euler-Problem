Prime = []

Total = []

N = 10000000

a = [False, False] + [True] * (N - 1)

Sum = 0

for i in range (1, N + 1):

    if a [i] :

        Prime.append (i)

        for j in range (2 * i, N + 1, i):

            a [j] = False

for i in Prime :

    N = len (str (i))

    Num_List = []

    List = []

    for j in range (1, N + 1) :

        Num_List.append (j)

    for j in str (i) :

        List.append (int (j))

    if (sorted (List) == Num_List) :

            Total.append (i)

print (Total [-1])