cnt = 0
from itertools import product
for val in product("ЗЕРКАЛО",repeat=6):
    val = "".join(val)
    if 1<= val.count("К")<=4:
            for i in "ЗЕРАЛО":
                if val.count(i)>1:
                    break
            else:
                cnt+=1
print(cnt)