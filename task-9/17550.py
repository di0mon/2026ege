with open (r".\files\17550.txt") as file:
    data = [list(map(int,i.split())) for i in file]
    cnt=0
for line in data:
    u = [line.count(i)for i in set(line)]
    if sorted(u)==[1,1,1,3]:
        pov= [ i for i in line if line.count(i) !=1]
        n_pov = [i for i in line if line.count(i) == 1]
        sqrt= sum(pov)**2
        sqrt1= sum(n_pov)**2
        if sqrt> sqrt1:
            cnt+=1
print(cnt)