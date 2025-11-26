def conv(num,sys):
    res =""
    while num:
        res+=(num%sys)
        num//=sys
    return res[::-1]
for N in range(1,100000):
    R = conv(N,4)
    if R.count()