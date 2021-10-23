Max = 0

for a in range (1, 100) :

    for b in range (1, 100) :

        list = []

        N = 0

        Sum = 0

        for i in str (a**b) :

            list.append (int (i))

            N = N + 1

        for i in range (0, N) :
            
            Sum = Sum + list [i]

        if (Sum > Max) :

            Max = Sum

print (Max)