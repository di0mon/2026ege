def conv(num, sys):
    res = ""
    while num !=0:
        res+=str(num%sys)
        num//=sys
    return res[::-1]
for N in range(1,1000):
    R = conv(N,3)
    if sum(map(int, R))//3==0:
        R="1" +R +"2"
    else:
        R= "2"+ R+"0"
    R = int(R,3)
    if R > 100:
        print(N,R)



