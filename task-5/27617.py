def conv(num, sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 100):
    R = conv(N, 2)
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += conv(sum(map(int, R)) * 3, 2)
    R = int(R, 2)
    ans.append([abs(130-R),N])
print(sorted(ans))
