from itertools import product
alph = sorted("СУБЛИМАЦЯ")
cnt = 0
for val in product(alph, repeat=5):
    cnt+=1
    val = "".join(val)
    if val[-1]!= "Я" and val.count("У") and val.count("И") and val.count("А") and val.count("Я") == 2:
        print(cnt)
