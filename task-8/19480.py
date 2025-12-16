from itertools import permutations

cnt = 0
for val in set(permutations("ПАРИЖАНКА")):
    val = "".join(val).replace("И", "А")
    if val.count("АА") == 1 and "AAA" not in val:
        cnt += 1
print(cnt)
