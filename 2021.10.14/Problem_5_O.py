from math import *

n = 20
b = 0

Num_ = [0] * (n+1)
Prime_ = []

product = 1

a = [False, False] + [True] * (n-1)

#소인수분해를 이용하기 위한 소수 구하기
for i in range (2, n+1):

    if a [i]:

      Prime_.append (i)

      b = b + 1

    for j in range (2 * i, n, i):

        a [j] = False

print (Prime_)

#내림차순
for i in range (0, n+1) :

  Num_[i] = n - i

#약수 제거
for i in range (0, n+1) :

  for j in range (i+1, n+1) :

    if (Num_[j]>0) :

      if (Num_[i]%Num_[j]==0) :

        Num_[j] = 0

print (Num_)

#다 곱하기
for i in range (0, n+1) :

  if (Num_[i]>0) :

    product = product * Num_[i]

product_copy = product

print (product)

#소수 나누기
for i in range (0, n+1) :

  for j in range (0, b) : 
    
    if (product%Prime_[j]==0) :

      product = product / Prime_[j]

    for k in range (0, n) :

        if (Num_[k]>0) :
          
          if (product%Num_[k]!=0) :

            product = product * Prime_[j]

        else :

          break

print (int (product))