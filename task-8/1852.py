cnt = 0
from itertools import product
for val in product("ГЕПАРД",repeat=5):
    val = "".join(val)
    if val.count("Г")==1 and val[0] not in "А" and val[-1] not in "Е":
        cnt+=1
print(cnt)