a_ = [0] * 1000
b_ = [0] * 1000
c_ = [0] * 1000
sum_ = [0] * 1000
a = 0
b = 0
c = 0
sum = 0

for i in range (1, 1000) :

    if (i%3==0) :

        if ((i%3==0) and (i%5==0)) : 

            c=c+1

            c_[c] = i

        if ((i%3==0) and (i%5!=0)) :
            
            a=a+1

            a_[a] = i

    elif ((i%3!=0) and (i%5==0)) :

        b=b+1

        b_[b] = i

for i in range (1, 1000) : 

    sum_[i] = a_[i] + b_[i] + c_[i]

    sum = sum + sum_[i]

print ("%d" % (sum))