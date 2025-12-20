from itertools import permutations

graph = "AD AB ED BE EG CG CF FB FA ".split()
matrix = "37 367 125 56 34 247 126".split()
print(*range(1, 9))
for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
