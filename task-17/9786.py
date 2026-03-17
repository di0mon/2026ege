with open(r".\files\17_9786.txt") as file:
    data = [int(i) for i in file]

m = max(i for i in data if abs(i)%100==25 )
ans=[]
for x,y,z in zip(data,data[1:],data[2:]):
    u1 = len(str(abs(x)))==4
    u2 = len(str(abs(y))) == 4
    u3 = len(str(abs(z))) == 4
    if u1+ u2 + u3<=2 and x+y+z<=m:
        ans.append(x+y+z)
print(len(ans),abs(max(ans)))


