from itertools import product
ans=0
cnt = 0
for val in product('АЖЗОПЮ', repeat = 6):
   cnt += 1
   val = ''.join(val)
   if cnt % 2 == 0 and val[0] == 'А' and val.count('З') >= 2:
       ans += 1
print(ans)