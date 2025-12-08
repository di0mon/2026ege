from itertools import product
cnt=0
for val in product("ПОЛИНА",repeat =8):
    s = val.count("П")+val.count("Л")+val.count("Н")
    if s>4:
        cnt+=1
print(cnt)