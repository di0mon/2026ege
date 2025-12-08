ans=[]
for N in range(1,100000):
    R = f"{N:b}"
    if sum(map(int,R))%2==0:
        R = "11" +R[2:]+"1"
    else:
        if R.count("1")>R.count("0"):
            R+="0"
        else:
            R+="1"
    R = int(R, 2)
    if R> 271:
        print(N)
        break




