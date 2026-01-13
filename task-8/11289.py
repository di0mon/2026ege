from itertools import *
from string import printable
cnt=0
for val in product(printable[:9], repeat=7):
    val="".join(val)
    if val[0]!= 0 and 