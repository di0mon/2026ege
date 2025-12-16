from itertools import permutations
cnt = 0
for val in set(permutations("СОРТИРОВКА")):
    val="".join(val)
    for m in "ОИА":
        val = val.replace(m, "*")
    for l in "СРТВК":
        val = val.replace(l, "!")
    if "!!!" not in val and "***" not in val:
        cnt+=1
print(cnt)