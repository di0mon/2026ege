def conv(num,sys):
    res=""
    while num:
        res +=str(num%sys)
        num//=sys
    return res[::-1]
for N in range(1,100000):
    R= conv(N,3)
    if N%3==0:
        R = "1"+R+"02"
    else:
        R+=conv((N%3)*4,3   )
    R=int(R,3)
    if R<100:
        print(R,N)
