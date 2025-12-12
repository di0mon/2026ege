ans=[]
for N in range(1,100000):
    R = f"{N:b}"
    if R.count("0")%2==0:
        R = "1" + R + "1"
    else:
        R+= "10"
    R = int(R,2)
    if R<100:
        ans.append(R)
print(ans)
