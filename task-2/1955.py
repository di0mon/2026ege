from itertools import*
def f(x,y,z,w):
    return not(y<=(x==w)) and (z<=x)

for a,b,c,d,e in product((0,1),repeat=5):
    table=[
        (a,1,1,b),
        (0,c,d,0),
        (e,0,1,0)
    ]
    if len(table)==len(set(table)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p,t)))for t in table]==[1,1,1]:
                print(*p,sep="")