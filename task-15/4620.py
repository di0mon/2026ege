def f(x,y):
    return (x+y<=22) or(y<=x-6) or(y>=A)
ans=[]
for A in range(0,1000):
    if all(f(x, y)for x in range (1, 1000)for y in range(1,1000)):
        ans.append(A)
print(max(ans))
