Prime = []

N = 10000

a = [False, False] + [True] * (N - 1)

for i in range (2, N + 1):

    if a [i] :

        if (i > 1000) :

            Prime.append (i)

        for j in range (2 * i, N + 1, i):

            a [j] = False

for i in range (len (Prime)) :

    for j in range (1, 4500 + 1) :

        if (Prime [i] + 2*j) <= Prime [-1] :

            List_1 = []
            List_2 = []
            List_3 = []

            for k in str (Prime [i]) :

                List_1.append (int (k))

            for k in str (Prime [i] + j) :

                List_2.append (int (k))

            if (sorted (List_1) == sorted (List_2)) :

                for k in str (Prime [i] + 2*j) :

                    List_3.append (int (k))
            
                if (sorted (List_1) == sorted (List_3)) :

                    if (((Prime [i] + j) in Prime) and ((Prime [i] + 2*j) in Prime)):

                        print ("".join (map (str, [Prime [i], Prime [i] + j,  Prime [i] + 2*j])), Prime [i], Prime [i] + j,  Prime [i] + 2*j, j)