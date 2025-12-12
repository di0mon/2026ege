from itertools import permutations
cnt=0
for val in set(permutations("ХОЧУ В ВУЗ")):
    val="".join(val)
    if val[0]not in "У" and val[0] not in" "and val[-1] !=" " and " У" not in val and "  "not in val:
        cnt+=1
print(cnt - 1)