with open (r".\files\17_15333.txt") as file:
    data =[int(i) for i in file]
max_19= max(i for i in data if i %19==0)
ans=[]
for x,y in zip(data,data[1:]):
    u= x>max_19
    u1= y>max_19
    if u+u1 >=1:
        ans.append(x+y)
print(len(ans),max(ans))
