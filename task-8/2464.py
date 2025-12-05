cnt = 0
from itertools import product
for val in product("НИЧЬЯ",repeat=7):
    val = "".join(val)
    for i in "ИЯ":
        val = val.replace(i,"*")
    if val.count("*") == 2 and "**" not in val:
        cnt+=1
print(cnt)