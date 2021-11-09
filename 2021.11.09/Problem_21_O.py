def Sum (N) :

    Total = 0

    for a in range (1, N) :

        if ((N % a) == 0) :

            Total = Total + a

    return (Total)

def Amicable_Numbers (N) :

    List = []

    for i in range (N + 1) :

        S = Sum (i)

        if (i != S) :

            if (i == Sum (S)) :

                List.append (i)

    return (List)

print (sum (Amicable_Numbers (10000)))