for N in range(1,10000):
    R=f"{2+N:b}"
    R+=str(R.count("1")%2)
    R+=str(R.count("1")%2)
    R=int(R, 2)
    if R<61:
        print(N,R)
