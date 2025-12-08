cnt = 0
from itertools import product

alph = sorted("ПАРУС")
for val in product(alph, repeat=5):
    val = "".join(val)
    cnt += 1
    if val[0] == "У" and val.count("А") > 0 and "АА" not in val:
        print(cnt)
        break
