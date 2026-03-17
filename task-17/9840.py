with open(r".\files\17_9786.txt") as file:
    data = (int(i) for i in file)

m = max(i for i in data if 1000<=i<=9999 and abs(i)%100==39 )
ans=[]
for x,y,z in zip(data,data[1:],data[2:]):
    u1 = len(str(x))==4
    u2= 1000 <= y <= 9999
    u3= 1000 <= z <= 9999
    if u1+ u2 + u3>=2 and x+y+z<=m:
        ans = ans.append(x+y+z)
print(len(ans),abs(max(ans)))