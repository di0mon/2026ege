def conv(num,sys):
    res =""
    while num:
        res+=str(num%sys)
        num//=sys
    return res[::-1]

for N in range(1,100000):
    R = conv(N,3)
    if N %3 != 0:
        R = "1" + R + R[-3:]
    else:
        R = conv(sum(map(int,R))*8,3)
    R = int(R,3)
    if 1000<= R<= 1300:
        print(R,N)
############################################


def conv(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]

ans = []
for n in range(1, 1000):
    r = conv(n, 3)
    if n % 3 != 0:
        r = '1' + r + r[-3:]
    else:
        r += conv(sum(int(i) for i in r) * 8, 3)
    r = int(r, 3)
    ans += [(abs(1220 - r), r)]
print(min(ans))


