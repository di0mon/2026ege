from functools import *

@lru_cache(None)
def f(n):
    if n >= 128:
        return f(n-5) + 1092
    else:
        return 5 * g(n-7) + 29

@lru_cache(None)
def g(n):
    if n > 303728:
        return n - 15
    else:
        return g(n+8) / 2 - 109

for i in reversed(range(301210)):
    g(i)

for i in range(55000):
    f(i)

print(f(2049))