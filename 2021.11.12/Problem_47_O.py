Num_List = []

Count = 4

for i in range (1, 140000) :

    List = []

    N = i

    j = 2

    while (i != 1) :

        if ((i % j) == 0) :

            List.append (j)

            i = i // j

        else :

            j = j + 1

    Set_List = list (set (List))

    for j in Set_List.copy () :

        if (List.count (j) > 1) :

            Set_List.append (j ** List.count (j))

            Set_List.remove (j)

    if (len (Set_List) == Count) :

        Num_List.append ([N, sorted (Set_List)])

for i in range (len (Num_List) - (Count - 1)) :

    T_F = True

    for j in range (1, Count) :

        if ((Num_List [i] [0] + j) != Num_List [i + j] [0]) :

            T_F = False
            
            break

    if (T_F == True) :
        
        if (len (list (set (Num_List [i] [1]) & set (Num_List [i + 1] [1]) & set (Num_List [i + 2] [1]) & set (Num_List [i + 3] [1]))) == 0) :

            print (Num_List [i])