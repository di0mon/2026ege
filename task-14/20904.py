def conv(num,sus):
    res =""
    while num:
        res += str(num%sus)
        num//=sus
    return res[::-1]

for x in range(1,2030):
    num_3 = conv(3**100-x,3)
    if num_3.count("0") ==1:
        print(x)
