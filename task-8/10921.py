from itertools import permutations
ans=0
for val in permutations("ДЖАВАСКРИПТ"):
    val="".join(val)
    cnt=0
    for i in range(len(val)):
        if val[i] =="А" or val[i]=="И":
            cnt+=(i+1)
        if cnt==11:
            ans+=1
print(ans)