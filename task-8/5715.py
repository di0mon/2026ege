cnt=0
for s in range(1,16):
    for s1 in range(s):
        for s2 in range(s1):
            res = s+s1+s2
            if res <=15:
                cnt+=1
print(cnt)