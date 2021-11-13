Max = [0, 0, 0]

Number = (10 ** 1000) - 1

for i in range (1, 1000) :

    for j in range (1, len (str (Number))) :

        T_F = False

        List = []

        N = (10 ** j) - 1

        for k in range (len (str (N))) :

            Num = int (N - ((10 ** k) - 1))

            if ((Num % i) == 0) :

                for a in str (Num) :

                    List.append (int (a))

                Count = List.count (9)

                if (Count > Max [2]) :

                    Max = [i, Num, Count]

                T_F = True

                break

        if (T_F == True) :

            break

print (Max)