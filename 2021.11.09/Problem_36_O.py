def Bin (N) :

    Bin_List = []

    Count = 0

    for i in bin (N) :

        if (Count == 0) :

            Count = 1

            continue

        if ((i == "0") or (i == "1")) :

            Bin_List.append (int (i))

    return (Bin_List)

Sum = 0

for i in range (1, 1000000) :

    List = []

    for j in str (i) :

        List.append (int (j))

    if ((len (List) % 2) == 0) :

        if (List [0 : (len (List) // 2)] == list (reversed (List [(len (List) // 2) : -1] + [List [-1]]))) :

            if ((len (Bin (i)) % 2) == 0) :

                if (Bin (i) [0 : (len (Bin (i)) // 2)] == list (reversed (Bin (i) [(len (Bin (i)) // 2) : -1] + [Bin (i) [-1]]))) :

                    Sum = Sum + i

                    print (i, Bin (i))

            if ((len (Bin (i)) % 2) != 0) :

                if (Bin (i) [0 : ((len (Bin (i)) - 1) // 2)] == list (reversed (Bin (i) [((len (Bin (i)) + 1) // 2) : -1] + [Bin (i) [-1]]))) :

                    Sum = Sum + i

                    print (i, Bin (i))

    if ((len (List) % 2) != 0) :

        if (List [0 : ((len (List) - 1) // 2)] == list (reversed (List [((len (List) + 1) // 2) : -1] + [List [-1]]))):

            if ((len (Bin (i)) % 2) == 0) :

                if (Bin (i) [0 : (len (Bin (i)) // 2)] == list (reversed (Bin (i) [(len (Bin (i)) // 2) : -1] + [Bin (i) [-1]]))) :

                    Sum = Sum + i
                    
                    print (i, Bin (i))

            if ((len (Bin (i)) % 2) != 0) :

                if (Bin (i) [0 : ((len (Bin (i)) - 1) // 2)] == list (reversed (Bin (i) [((len (Bin (i)) + 1) // 2) : -1] + [Bin (i) [-1]]))) :

                    Sum = Sum + i

                    print (i, Bin (i))

print (Sum + 25) # 25 = 1 + 3 + 5 + 7 + 9