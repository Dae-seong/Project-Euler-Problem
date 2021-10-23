list = []

Sum = 0

for i in range (0, 1000000) :

    for j in str (i) :

        list.append (int (j))

print (list)

print (list [1] * list [10] * list [100] * list [1000] * list [10000] * list [100000] * list [1000000])