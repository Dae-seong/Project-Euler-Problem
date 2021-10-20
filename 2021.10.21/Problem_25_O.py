list = [0] * 100000000

list [1] = 1
list [2] = 1

for i in range (3, 100000) :

    list [i] = list [i - 1] + list [i - 2]

    if (len (str (list [i])) == 1000) :

        print (i)

        break



