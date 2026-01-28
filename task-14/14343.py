def conv(num,sys):
    res=""
    while num:
        res+= str(num%sys)
        num//=sys
    return res[::-1]

num= 5*343**2031 + 4*49**2142 - 3*7**111+ 7**222
R = conv(num,7)
ans = sum(map(int,R))
print(ans)