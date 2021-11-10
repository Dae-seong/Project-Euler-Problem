Prime = []

N = 750000

a = [False, False] + [True] * (N - 1)

Count = 0

Sum = 0

for i in range (2, N + 1):

    if a [i] :

        Prime.append (i)

        for j in range (2 * i, N + 1, i):

            a [j] = False

for i in Prime :

    if (i > 9) :

        List_1 = []

        T_F = True

        for a in str (i) :

            List_1.append (int (a))

        N = len (List_1)

        List_2 = List_1.copy ()

        for j in range (N - 1) :

            List_1.pop (0)

            if int ("".join (list (map (str, List_1)))) not in Prime :

                T_F = False

                break

        if (T_F == True) :

            for j in range (N - 1) :

                List_2.pop ()

                if int ("".join (list (map (str, List_2)))) not in Prime :

                    T_F = False
                    
                    break

        if (T_F == True) :

            Count = Count + 1

            Sum = Sum + i

            print (i)

print (Count, Sum) 