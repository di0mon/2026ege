from itertools import permutations

graph = "AF AD AB DF DC CE CB BG GE EF".split()
matrix = "457 567 45 136 123 247 126".split()
print(*range(1, 9))
for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
