def f(start,end,cnt=0):
    if start==end:return 1
    if start>end:return 0
    return f(start+1,end)+f(start+5,end)+f(start*3,end)
print(f(1,[1000,1024],8))