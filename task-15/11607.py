def DEL(n, m):
    return n % m == 0


def f(x):
    return not (DEL(x, 263) <= DEL(x, A)) and DEL(x, 71)

for A in range(1, 1000):
    if all(f(x) for x in range(1, 100000)):
        print(A)
