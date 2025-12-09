def conv(num,sys):
    res =""
    while num:
        res+=str(num%sys)
        num//=sys
    return res[::-1]
for N in range(1,100000):
    R = conv(N, 9)
    if R[0]==7:
        R = R.replace("6","*")
        R = R.replace("3", "6")
        R = R.replace("*", "3")
        R = "34" + R
    else:
        R= "3"+ R[1:] + "45"
    R=int(R,9)

        print(N,R)