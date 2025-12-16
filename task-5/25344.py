def conv(num, sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 100000):
    R = conv(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += conv(sum(map(int, R)) * 3, 3)
    R = int(R, 3)
    if R > 208 and R%2!=0:
        ans.append(R)
print(min(ans))
