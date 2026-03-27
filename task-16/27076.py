from functools import lru_cache
@lru_cache
def F(n): #2026 ->42(-)
    if n < 43: return G(n + 4)
    return 2 * F(n - 2) - F(n - 4) + 2

@lru_cache
def G(n): #46->11_241
    if n < 11_240: return G(n + 3) + 2
    return Q(n)

@lru_cache
def Q(n): #11_240 ->
    if n < 21: return n + 4
    return Q(n - 4) + 2
for i in range(21,11240):
    Q(i)

for i in range(11240,46,-1):
    G(i)

print(F(2026))


###########################
Q = [0] *12000
for i in range(12000):
        if i <21: Q[i] = i +4
        else: Q[i] = Q[i-4]+ 2


G = [0] *12000
for i in range(12000,0,-1):
        if i <11240:G[i] = G[i+3]+2
        else: G[i] =Q[i]
