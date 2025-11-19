for N in range(1,1000):
    try:
        if 41%N==2 and 131%N==1:
            print(N)
            break
    except:
            pass