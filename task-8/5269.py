from itertools import permutations
cnt =0
for val in set(permutations("АМФИБРАХИЙ")):
    val="".join(val)
    if val[5] == "Б" and val[6] =="Р":
        cnt+=1
    print(cnt)