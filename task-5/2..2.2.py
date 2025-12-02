a =[]
for N in range(151,100000):
    R = f"{N:x}"
    R.replace("A","1")
    if (R.count("0")+R.count("2")+R.count("4")+R.count("6")+R.count("8")+R.count("A")+R.count("C")+R.count("E")+R.count("F")) > 2:
        R+="B"
    else:
        R = "F" + R
    R= int(R,16)
    if R >3500:
        print(R,N)
