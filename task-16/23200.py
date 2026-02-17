from functools import lru_cache
@lru_cache(None)
def F(n):
    if n<=10:return n
    return 3n + F(n-3)


