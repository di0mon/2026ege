def conv(num,sys):
    res =""
    while num:
        res +=str(num%sys)
        num//=sys
    return res[::-1]
cnt=0
R = "15*343**2031 + 7*49**1142 - 3*7**111 + 7**222 - 16809"
cnt+= (R.count("0")+R.count("2")+R.count("4")+R.count("6")-(R.count("1")+R.count("3")+R.count("5")+R.count("7"):
print(cnt))


