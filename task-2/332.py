# print("x,y,w,z")
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 f = ((x or y) and not z) and not w
#                 if f
#                     print(x,y,z,w)



from itertools import *
def f(x,y,z,w):
    table=[
        (1,0,0,0),
        (0,0,1,0),
        (0,1,0,1),
]
for p in permutations("xyzw"):
    if[f(**dict(zip(p,t)))for t in table]==[1,0]:
        print
