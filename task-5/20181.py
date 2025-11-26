for N in range(1, 100000):
    R = f"{N:b}"
    if N % 2 ==0:
        R += bin(R.count("1"))[2:]
    else:
        R = "1" + R + "101"
    R = int(R, 2)
    if R > 350:
        print(N)
        break
