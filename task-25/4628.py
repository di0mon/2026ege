from itertools import *
from string import *
ans=[]
for V in printable[:10]:
    for l in range(0,3):
        for Z in product(printable[:10],repeat=l):
            num=int(f"12{"".join(Z)}4{V}65")
            if num%61==0:
                ans.append([num,num//161])
for i in sorted(ans):
    print(*i)