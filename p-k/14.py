def conv(num, sys):
    res = ""
    while num !=0:
        res+=str(num%sys)
        num//=sys
    return res[::-1]
for x in range(66902,66907):
    num = conv(5**2025 + 5**400 - x,5)
    print(num)