list = [0] * 1000000
List = [0] * 1000000

N = 0

Max = 0
 
for a in range (1, 9 + 1) :

    for b in range (0, 9 + 1) :

        for c in range (0, 9 + 1) :

            for d in range (0, 9 + 1) :

                for e in range (0, 9 + 1) :

                    for f in range (1, 9 + 1) :

                        if ((a == f) and (b == e) and (c == d)) :

                            list [N] = 100000*a + 10000*b + 1000*c + 100*d + 10*e + f

                            for i in range (100, 999 + 1) :

                                if (((list [N] % i) == 0)) :

                                    if (((list [N] / i) > 100) and ((list [N] / i) < 999)) :

                                        List [N] = list [N]

                                        break

                            N = N + 1

for i in range (0, 10000) :

    if (List [i] > 0) :
        
        if (List [i] > Max) :

            Max = List [i]
N = 0

print ("%d = " % (Max), end = "")

for i in range (100, 999 + 1) :

    if ((Max % i) == 0) :

        if (((Max / i) > 100) and ((Max / i) < 999)) :

            if (N == 1) :

                print ("%d" % (i))

                break

            print ("%d * " % (i), end = "")

            N = N + 1