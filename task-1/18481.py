from itertools import *
graph="AC BC AB CE EG ED BD DF FG".split()
matrix="67 567 457 35 234 12 123".split()
print(*range(1,9))
for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)


