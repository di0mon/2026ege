def conv(a):
    if a == 0:
        return "0"
    s =""
    while a>0:
        s = str(a%3)+s
        a = a//3
    return s
ans =[]
for N in range(1,100000):
    R = conv(N)
    if N.count("")
