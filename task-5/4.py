def conv(num,sus):
    res =""
    while num:
        res +=str(num%sus)
        num//=sus
    return res[::-1]
ans =[]
for N in range(1,100000):
    R =conv(N,3)
    if sum(map(int,R))% 3 == 0:
        R += "212"
    else:
        R += conv(sum(map(int,R))*2,3)
    R = int(R, 3)
    if R>490:
        ans.append(R)
print(min(ans))


