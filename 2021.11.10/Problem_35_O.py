Prime = []

N = 1000000

a = [False, False] + [True] * (N - 1)

Count = 0

for i in range (2, N + 1):

    if a [i] :

        Prime.append (i)

        for j in range (2 * i, N + 1, i):

            a [j] = False

def Function (N) :

    

    return (List)

for i in Prime :

    List = []

    T_F = True

    for a in str (i) :

        List.append (int (a))

    for j in range (len (List) - 1) :

        List.append (List [0])
        List.remove (List [0])

        if int ("".join (list (map (str, Function (i))))) not in Prime :

            T_F = False

            break

    if (T_F == True) :

        Count = Count + 1

        print (i)

print (Count)        