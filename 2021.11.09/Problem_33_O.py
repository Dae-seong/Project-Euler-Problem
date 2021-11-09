from fractions import *

Product = 1

for i in range (1, 100) :

    for j in range (i, 100) :

        if (i != j) :
        
            A = [int (k) for k in str (i)] # 분자
            B = [int (k) for k in str (j)] # 분모

            if ((A [-1] != 0) or (B [-1] != 0)) :

                T_F = False

                for k in B :

                    if k in A :

                        A.remove (k)
                        B.remove (k)

                        T_F = True

                if ((len (A) > 0) and (len (B) > 0)) :

                    A = int ("".join (list (map (str, A))))
                    B = int ("".join (list (map (str, B))))
                    
                    if (T_F == True) :

                        if ((B != 0) and (Fraction (A, B) == Fraction (i, j))):

                            Product = Product * Fraction (i, j)

print (Product)