from itertools import*
graph="АД АЕ АК ЕВ ВД ДГ ГБ ГК КБ БЖ ЖЕ".split()
matrix="248 137 268 15 467 357 256 12".split()
print(*range(1,9))
for i in permutations("АБВГДЕЖК"):
    if all(str(i.index(x)+1)in matrix[i.index(y)]for x,y in graph):
        print(*i)