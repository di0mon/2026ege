from itertools import *
from string import printable

cnt = 0
for val in product(printable[:7], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        for i in printable[:7:2]:
            val = val.replace(i, '*')
        for i in printable[1:7:2]:
            val = val.replace(i, '!')
        if val.count('**') > 1 and '***' not in val:
            cnt += 1
print(cnt)
