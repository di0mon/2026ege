from itertools import permutations
graph = "АБ БВ АВ ВД ДЕ ЕВ ЕК КГ КЕ ГВ".split()
matrix = "24 16 56 1267 36 23457 46 ".split()
print(*range(1, 9))
for i in permutations("АБВГДЕК"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
