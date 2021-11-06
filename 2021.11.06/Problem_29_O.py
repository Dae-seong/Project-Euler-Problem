List = []

for a in range (2, 100 + 1) :

    for b in range (2, 100 + 1) :

        List.append (a**b)

List = list (set (List))

print (len (List))