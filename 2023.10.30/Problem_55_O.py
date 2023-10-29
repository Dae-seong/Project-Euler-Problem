result = 0

for i in range (1, 10000 + 1) :

    k = i

    for j in range (50) :

        k = k + int (str (k) [::-1])

        if (str (k) == str (k) [::-1]) : break

    else : result += 1; print (i)

print (result)