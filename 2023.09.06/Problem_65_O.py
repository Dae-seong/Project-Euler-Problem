def recursion (k, N, array) :

    a, b = array [0], array [1]

    if (k == N + 1) : return b, a

    a, b = b, a + 2 * (N - k + 1) * b
    a, b = b, a + b
    a, b = b, a + b

    return recursion (k + 1, N, [a, b])

N = 100

array = [0, 1] if (N % 3 == 0) else [1, 1] if (N % 3 == 1) else [1, 2]

a, b = recursion (0, N // 3 - 1, array)

print (a + b, b)

print (sum ([int (i) for i in str (a + b)]))