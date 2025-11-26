def conv(num, sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for x in range(1, 2400):
    num_3 = conv(7 * 9 ** 210 + 6 * 9 ** 110 - x, 9)
    if num_3.count("0") == 100:
        print(x)
