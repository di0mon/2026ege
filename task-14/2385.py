def conv(num,sus):
    res =""
    while num:
        res +=str(num%sus)
        num//=sus
    return res[::-1]
num = 16**820 - 2**761 + 14

print(conv(num,4).count("0"))
######################################
num = 16**820 - 2**761 + 14

cnt_0 = 0
while num:
    if num % 4 == 0:
        cnt_0+=1
    num//=4
print(cnt_0)

