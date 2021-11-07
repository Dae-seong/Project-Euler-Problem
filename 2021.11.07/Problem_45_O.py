P = []
H = []

for n in range (1, 100000) :

    P.append (int ((n * (3*n - 1)) / 2))

for n in range (1, 100000) :

    H.append (int (n * (2*n - 1)))

for i in range (len (P)) :

    if (H [i] in P) :

        if (H [i] > 40755) :

            print (H [i])

            break