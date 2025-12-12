from itertools import permutations

cnt = 0
for val in set(permutations("ПРОБНИК", r=7)):
    val = "".join(val)
    if "ОИ" not in val and "ИО" not in val and val[0] in "ПРБНК" and val[-1] in "ПРБНК":
        cnt += 1
print(cnt)
