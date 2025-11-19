ans =[]
num =51*7**12 - 7**3 - 22
while num>0:
    ans += [num%7]
    num = num//7
print(sum(ans))