Prime = [2, 3, 5, 7, 11, 13, 17]

Num_List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Sum = 0

for a in range (1, 9 + 1) :

    for b in range (0, 9 + 1) :

        if (a != b) :

            for c in range (0, 9 + 1) :

                if (a != c) and (b != c) :

                    for d in range (0, 9 + 1) :

                        if (a != d) and (b != d) and (c != d) :

                            for e in range (0, 9 + 1) :

                                if (a != e) and (b != e) and (c != e) and (d != e) :

                                    for f in range (0, 9 + 1) :

                                        if (a != f) and (b != f) and (c != f) and (d != f) and (e != f) :

                                            for g in range (0, 9 + 1) :

                                                if (a != g) and (b != g) and (c != g) and (d != g) and (e != g) and (f != g) :

                                                    for h in range (0, 9 + 1) :

                                                        if (a != h) and (b != h) and (c != h) and (d != h) and (e != h) and (f != h) and (g != h) :

                                                            for i in range (0, 9 + 1) :

                                                                if (a != i) and (b != i) and (c != i) and (d != i) and (e != i) and (f != i) and (g != i) and (h != i) :

                                                                    for j in range (0, 9 + 1) :

                                                                        if (a != j) and (b != j) and (c != j) and (d != j) and (e != j) and (f != j) and (g != j) and (h != j) and (i != j) :
                                                                    
                                                                            List = [a, b, c, d, e, f, g, h, i, j]

                                                                            l = 0

                                                                            T_F = True

                                                                            if (sorted (List) == Num_List) :

                                                                                for k in Prime :

                                                                                    l = l + 1

                                                                                    N = int ("".join (map (str, List [l : l + 3])))

                                                                                    if ((N % k) != 0) :

                                                                                        T_F = False

                                                                                        break

                                                                                if (T_F == True) :

                                                                                    Sum = Sum + int ("".join (map (str, List)))

print (Sum)