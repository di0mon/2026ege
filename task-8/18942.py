from itertools import product
cnt = 0
alph = sorted("ДИОНСЙ")
for val in product(alph, repeat=6):
    val ="".join(val)
    if ("Д" in val and "H" not in val) ("H" in val and "Д" not in val):

