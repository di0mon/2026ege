from itertools import product
cnt=0
for val in product('КОТБУС', repeat=8):
    val = "".join(val)
    if val[0] not in "ОУ" and "КОТ" in val:
        cnt+=1
print(cnt)