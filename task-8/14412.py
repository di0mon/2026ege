from itertools import product
cnt = 0
alph = sorted("АЛГОРИТМ")
for val in product(alph, repeat=6):
    val = "".join(val)
    if val[0] !="Р" and val[-1] not in "ЛГРТМ" and val.count("Л")<2:
        cnt+=1
print(cnt)