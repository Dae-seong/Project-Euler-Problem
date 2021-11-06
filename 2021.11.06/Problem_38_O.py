Num_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Total = []

for a in range (1, 10000) :

    List = []

    Sum = 0

    for n in range (1, 10 + 1) :

        Sum = Sum + len (str (a * n))

        if (Sum >= 9) :

            break

    if (Sum == 9) :

        for n in range (1, 10 + 1) :

            if (n == 1) :

                for i in str (a) :

                    List.append (int (i))

            if ((n > 1) and (len (List) < 9)) :

                for i in str (a * n) :

                    List.append (int (i))

            if (len (List) > 9) :

                break

            if (len (List) == 9) :

                if (sorted (List) == Num_List) :

                    Total.append (List)

print (*Total [-1])