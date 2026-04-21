from itertools import *
def f(x,w,y,z):
    return ((w<=z) == x<= (not y)) or (x and z)

for a,b in product((0,1),repeat=2):
    table =[
        (1,0,0,1),
        (1,1,1,0),
        (0,a,0,b)
    ]
    if len(table)== len(set(table)):
        for p in permutations("xywz"):
           if [f(**dict(zip(p,t)))for t in table] ==[1,0,1]:
               print(*p,sep="")


