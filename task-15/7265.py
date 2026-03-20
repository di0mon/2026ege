def DEL(n, m):
    return n % m == 0


def f(x):
    return (DEL(x, 2) <= (not DEL(x, 3))) or (x + A >= 100)

for A in range(1, 1000):
    if all(f(x) for x in range(1, 100000)):
        print(A)
        break