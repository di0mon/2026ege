def f(x,y):
    return (A<x) or (x**2 - 7*x+10>0) and (A>=y) or (y**2+7*y+12)>0
ans=[]
for A in range(0,1000):
    if all(f(x, y)for x in range (1, 1000)for y in range(1,1000)):
        ans.append(A)
print(max(ans))
