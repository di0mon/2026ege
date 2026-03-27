with open (r".\files\14251.txt") as file:
    data =[list(map(int,i.split()))for i in file]
cnt = 0
for line in data:
    u = [line.count(i) for i in set(line)]
    if sorted(u) ==[1,1,1,2,2]:
        pov= [i for i in line if line.count(i) !=1]
        ne_pov= [i for i in line if line.count(i) ==1]
        if sum(pov) <= sum(ne_pov):
            print(sum(line))
            break
