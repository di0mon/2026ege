cnt = 0
from itertools import product
for val in product("ПСКАЛЬ",repeat=5):
    val = "".join(val)
    if val[0]!="Ь" and "ЬЬ" not in val:
        cnt+=1
print(cnt)