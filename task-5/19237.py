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
    if N % 3 ==0:
        R += R[-2:]
    else:
        R += str(conv(sum(map(int,R))))
    R = int(R,3)
    if R%2 ==0 and R>220:
        ans.append(R)
print(min(ans))



