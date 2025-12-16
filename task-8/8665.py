from itertools import product
from string import printable
cnt = 0
for val in product(printable[:12],repeat =7):
    val = "".join(val)
    if