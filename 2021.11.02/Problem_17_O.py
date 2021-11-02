list = [[""], 
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "-"], 
        ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seven-teen", "eighteen", "nineteen"], 
        ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"], 
        ["one hundred and", "two hundred and", "three hundred and", "four hundred and", "five hundred and", "six hundred and", "seven hundred and", "eight hundred and", "nine hundred and"]]

Sum = [0] * 100

def function (n) :

    List = [0]

    for k in str (list [n] [i]) :

        List.append (k)

    return (List.count ("-") + List.count (" "))

for i in range (0, 10) :

    Sum [1] = Sum [1] + len (list [1] [i]) - function (1) # 1 ≤ n ≤ 9 자리수 합

    Sum [2] = Sum [2] + len (list [2] [i]) - function (2) # 10 ≤ n ≤ 19 자리수 합

for i in range (0, 8) :

    Sum [3] = Sum [3] + (len (list [3] [i]) - function (3)) * 10 + Sum [1] # 20 ≤ n ≤ 99 자리수 합

for i in range (0, 9) :

    Sum [4] = Sum [4] + (len (list [4] [i]) - function (4)) * 100 + (Sum [1] + Sum [2] + Sum [3] - len ("and")) # 100 ≤ n ≤ 999 자리수 합

print (sum (Sum) + len ("one thousand") - 1)