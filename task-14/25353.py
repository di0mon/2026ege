from string import printable as alph
def conv(num,sys):
    res=""
    while num:
        res += alph[num%sys]
        num//=sys
    return res[::-1]

for x in range(1,27001):
    num=conv(3*27**9 + 2*27**6 + 27**3 -x,27)
    if num.count("0")==6:
        print(x)
        break