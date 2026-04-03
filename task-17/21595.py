with open(r".\files\17_21595.txt") as file:
    data = [int(i) for i in file]

m = max(i for i in data if len(i)==4 and )
ans=[]
for x,y,z in zip(data,data[1:],data[2:]):
        ans.append(x+y+z)
print(len(ans),abs(max(ans)))