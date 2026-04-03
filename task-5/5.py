def conv(num,sys):
    res =""
    while num:
        res += (num%sys)
        num//=sys
    return res[::-1]

for N in range(1,100000):
    R = conv(N,4)
    if N %4==0:
        R+= R[:2]
    else:
        R+= conv((N%4)*4,4)
    R= int(R,4)
    if R>291:
        print(R,N)