for x in range(1,3000):
    ans = 9 * 11 ** 210 + 8 * 11 ** 150 - x
    cnt = 0
    while ans > 0:
        if ans % 11 == 0:
            cnt += 1
        ans = ans // 11
    if cnt == 60:
        print(x)
