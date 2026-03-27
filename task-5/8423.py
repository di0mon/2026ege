for N in range(1,2000000):
    R = f"{N:b}"
    if N%5==0:
        R+= f"{5:b}"
    else:
        R+="1"
    if int(R,2)%7==0:
        R+= f"{7:b}"
    else:
        R+="1"
    R = int(R,2)
    if R<1855663:
        print(N,R)