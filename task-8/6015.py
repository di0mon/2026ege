from itertools import *
from string import *
cnt = 0

for val in product(digits[:9], repeat=7):
    val="".join(val)
    if val[0] !="0" and val.count("8")==1 and val[-1] not in "02468" and val[0] not in "1357":
        cnt+=1
print(cnt)
