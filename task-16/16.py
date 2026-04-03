from functools import lru_cache

def F(n):
    3*(G(n-2)+5)
@lru_cache()
def G(n):
    if n>=8: return G(n-3)+2
    else:3*n

print(F(12345))

