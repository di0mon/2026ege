for N in range(1, 100000):
    R = f"{N:b}"
    if R.count("1") % 2 ==0:
        R = R + "10"
    else:
        R = "1" + R[2:] + "01"
    R = int(R, 2)
    if R < 30:
        print(N)
        break