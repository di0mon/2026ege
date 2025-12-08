for N in range(1,100000):
    R= f"{N:b}"
    if R.count("1") % 5 == 0:
        f()
