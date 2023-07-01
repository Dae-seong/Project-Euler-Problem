from math import *

Prime = []

N = 1000000

find_mul = 8

a = [False, False] + [True] * (N - 1)

for i in range (2, N + 1):

  if a [i]:

    Prime.append (i)

    for j in range (2 * i, N + 1, i):

        a [j] = False

p_c_list = []

for p in Prime :

    p_list = []
   
    count_dict = {}
    count_set = set ()

    for c in str (p) :
       
       p_list.append (int (c))

    for i in range (0, 9 + 1) :
    
        if p_list.count (i) == 0 :
            
            pass

        else :
            
            count_dict [i] = p_list.count (i)
            count_set.add (p_list.count (i))

    if list (count_set) [-1] == 1 :
       
        del count_dict

    else :

        p_c_list.append ([p, count_dict])

Mul_p_list = [[], [], [], [], [], [], [], [], [], []]

for i in range (1, len (p_c_list)) :

    value_list = []
    
    for key, value in p_c_list [i] [1].items () :

        value_list.append (value)

    Mul_p_list [max (value_list)].append (p_c_list [i] [0])

p_list = []

for i in range (len (Mul_p_list) - 7, len (Mul_p_list)) :

    Mul_list = []

    for j in range (i, len (Mul_p_list)) :

        Mul_list = Mul_list + Mul_p_list [j]

    for p in Mul_p_list [i] :

        c_list = []

        count = 1
        not_count = 0

        for c in str (p) :

            c_list.append (int (c))

        for j in c_list :

            if (c_list.count (j) == i) :

                Mul_num = j
                
                break

        for k in range (0, 9 + 1) : # 바꾸는 수

            c_copy = c_list.copy ()

            if k != Mul_num :

                for j in range (len (c_list)) :

                    if c_list [j] == Mul_num :

                        c_copy [j] = k

                new_p = int ("".join (map (str, c_copy)))

                if new_p in Mul_list:

                    count = count + 1

                else :

                    not_count = not_count + 1

                    if not_count == (11 - find_mul) :

                        break

        if count == find_mul :

            p_list.append ([p, count])

for i in range (len (p_list)) :

    if (p_list [i] [1] == find_mul) :

        print (p_list [i])

        break
