from string import printable as alph
from itertools import product
cnt=0
for val in product(alph[9:],repeat =4):
    val="".join(val)
    if val[0]!="0":
        if val.count("8")==1 and val
            cnt+=1
            print(cnt)