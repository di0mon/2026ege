from itertools import permutations

graph = "AB AF AC CE CD DH HE EG GF FB FA".split()
matrix = "68 47 45 237 368 158 248 157".split()
print(*range(1, 9))
for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
