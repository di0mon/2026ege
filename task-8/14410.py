ans=0
from itertools import product

alph=sorted("СОЛНЦЕ")
for pos, val in (enumerate(product(alph, repeat=6),start=1)):
    val ="". join(val)
    if pos % 2 ==0 and val[0] not in "ОE" and val.count("Ц")==2:
        ans+=1
print(ans)