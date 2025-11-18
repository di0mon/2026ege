def conv(num,sus):
    res =""
    while num:
        res +=str(num%sus)
        num//=sus
    return res[::-1]
num =4*625**9 - 25**15 + 2*5**11 - 7

print(conv(num,5).count("4"))

###########################################

num =4*625**9 - 25**15 + 2*5**11 - 7

cnt_4 = 0
while num:
    if num % 5 == 4:
        cnt_4+=1
    num//=5
print(cnt_4)