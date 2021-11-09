Count = 0

for a in range(0, 2 + 1) :

    if ((a * 100) == 200) :

        Count = Count + 1
        
        break

    else :

        for b in range (0, 4 + 1) :

            if (((a * 100) + (b * 50)) == 200) :

                Count = Count + 1

                break

            else :

                for c in range (0, 10 + 1) :

                    if (((a * 100) + (b * 50) + (c * 20)) == 200) :

                        Count = Count + 1

                        break

                    for d in range (0, 20 + 1) :

                        if (((a * 100) + (b * 50) + (c * 20) + (d * 10)) == 200) :

                            Count = Count + 1

                            break

                        else :

                            for e in range (0, 40 + 1) :

                                if (((a * 100) + (b * 50) + (c * 20) + (d * 10) + (e * 5)) == 200) :

                                    Count = Count + 1

                                    break

                                else :

                                    for f in range (0, 100 + 1) :

                                        if (((a * 100) + (b * 50) + (c * 20) + (d * 10) + (e * 5) + (f * 2)) == 200) :

                                            Count = Count + 1

                                            break

                                        else :

                                            for g in range (0, 200 + 1) :

                                                if (((a * 100) + (b * 50) + (c * 20) + (d * 10) + (e * 5) + (f * 2) + (g * 1)) == 200) :

                                                    Count = Count + 1

                                                    break

print (Count + 1)