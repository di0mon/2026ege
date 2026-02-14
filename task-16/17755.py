# from functools import lru_cache
#
# @lru_cache(None)
def F(n):
    if n>=400: return n
    return n+ 6+F(n+12)


print(F(72)-F(108))