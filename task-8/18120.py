from itertools import product
num=0
cnt=0
for val in product("ЕЛОПРСТ",repeat = 5):
    pos="".join(val)
    num+=1
    if num%2==1 and pos[-1] in "ЕО":
        sogl = 0
        for l in" ЛПРСТ":
            sogl += pos.count(l)
        if sogl<=3:
            cnt+=1
print(cnt)