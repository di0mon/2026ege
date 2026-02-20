from itertools import permutations

cnt =0
for val in permutations("0123456789",r=4):
    val = "".join(val)
    if val[0]!=0:
        val = val.replace("2","0").replace("4","0").replace("6","0").replace("8","0")
        val = val.replace("3","1").replace("5","1").replace("7","1").replace("9","1")
        if "11" not in val and "00" not in val:
            cnt+=1
print(cnt)

