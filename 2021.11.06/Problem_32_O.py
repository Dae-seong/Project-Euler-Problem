Total = []

Num_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def Function (N) :

    for i in str (N) :

        List.append (int (i))

for a in range (1, 10000) :

    for b in range (a, 10000) :

        List = []

        Function (a)

        Function (b)

        Function (a * b)

        if (len (List) == 9) :

            List.sort ()

            if (List == Num_List) :

                Total.append (a * b)

Total = list (set (Total))

print (sum (Total))