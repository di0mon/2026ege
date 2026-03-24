with open (r".\files\17628.txt") as file:
    data = [list(map(int,i.split())) for i in file]
    cnt=0
for line in data:
    u = [line.count(i)for i in set(line)]
    if sorted(u)==[1,1,1,1]:
        maxx = max(line)
        minn= min(line)
        n= maxx+minn
        s_ost= sum(line)-(maxx + minn)
        if n <= s_ost:
            cnt+=1
print(cnt)