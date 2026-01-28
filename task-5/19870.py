def conv(num,sys):
    res=""
    while num:
        res +=str(num%sys)
        num//=sys
    return res[::-1]
for N in range(1,100000):
    R = conv(N,4)
    if  R.count("0")+R.count("1")+R.count("2")+R.count("3")% 2 == 0:
        R="12"+R
    else:


