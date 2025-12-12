from itertools import*
from string import printable
cnt=0
for val in product(printable[:12], repeat =7):
    val = "".join(val)
    if val[0]!= "0":
        new_val=""
        for i in val:
            if int(i,12)%3==0:
                new_val+="*"
            else:
                new_val+="!"
        if "!!" not in new_val and "**" not in new_val:
            cnt+=1
print(cnt)