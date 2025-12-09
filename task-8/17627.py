from itertools import product
from string import printable
cnt=0
for val in product(printable[:15], repeat=5):
    val = "".join(val)
    if val[0] != "0" and val.count("8") == 1:
       # cnt9 = 0
       # for x in printable[10:15]:
            #cnt9 += val.count(x)
       if sum([val.count(x) for x in printable[10:15]])>=2:
           cnt+=1
print(cnt)