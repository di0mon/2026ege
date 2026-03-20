with open (r".\files\17_11236.txt") as file:
    data= ( int(i) for i in file)
minn = min(i for i in data if 10<=abs(i)<=99)
q=minn^2
ans=[]
for x,y,z in zip(data,data[:1],data[:2]):
    u1= x > q
    u2= x > q
    u3= x > q
    if (u1+u2+u3) == 2:


