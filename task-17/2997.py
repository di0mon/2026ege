with open(r".\files\17_2997.txt") as file:
    data = (int(i) for i in file)
q = [int(str(abs(i))[1]) for i in data if len(str(abs(i)))==3]
moda = max((q.count(i),i) for i in range(10))[1]
ans=[]
for x,y in zip(data,data[:1]):
    u1 = x[-1:] == moda
    u2 = x[-1:] == moda
    if u1+u2 >=1:
        ans.append(x + y)
print(len(ans), (max(ans)))

