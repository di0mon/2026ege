def conv(a):
    if a == 0:
        return "0"
    s = ""
    while a > 0:
        s = str(a%3)+ s
        a = a//3
    return s

for N in range(1,10000):
    R = conv(N)
    if sum(map(int,R))%2 ==0:
        R ="12" + R[2:] + "0"
    else:
        R ="10" + R[2:] + "2"
    R = int(R,3)
    if R >105:
        print(N)
        break