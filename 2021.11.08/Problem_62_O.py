Sort_List = []

Num_List = []

N = 3

for i in range (1000, 10000) :
    
    List = []

    for k in str (i ** N) :

        List.append (int (k))

    Sort_List.append (sorted (List))

    Num_List.append (List)

for i in range (len (Sort_List)) :

    if (Sort_List.count (Sort_List [i]) == 5) :

        print (Sort_List.count (Sort_List [i]), Sort_List [i], int ("".join (map (str, Num_List [i]))))