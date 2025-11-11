ans=[]
from string import printable as alph
def convert2(num, sus):
    res = ""
    while num != 0:
        res += alph[num % sus]
        num //= sus
    return res[::-1]

for N in range(1,100000):
    R = convert2(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += convert2((N % 3) * 5, 3)
    R = int(R, 3)
    if R>133:
        ans.append(R)
print(min(ans))

