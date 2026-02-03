from itertools import*

def f(x,y,z,w):
    return x==(y<=(z or x)) and w
for a,b,c,d,e in product((0,1),repeat=5):
    table=[
        (1,0,1,a),
        (0,b,c,0),
        (1,0,d,e),
    ]
    if len(table)== len(set(table)):
        for p in permutations("xyzw"):
            if[f(**dict(zip(p,t))) for t in table]==[1,1,1]:
                print(*p,sep="")



