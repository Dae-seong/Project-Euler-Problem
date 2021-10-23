Sum = 0

list = []

def Function (x) :

    return x**x

for i in range (1, 1000 + 1) :

    Sum = Sum + Function (i)

for i in str (Sum) :

    list.append (int (i))

for i in range (-10, 0) :

    print (list [i], end = "")