def f(A):
    for x in range(0,1000):
        for y in range(0,1000):
            F =(2*x+y!=70) or (x<y) or (A<x)
            if not F:
                return False
    return True

for A in range(1000,-1000,-1):
    if f(A):
        print(A)
        break

def f(x, y):
    return (2 * x + y != 70) or (x < y) or (A < x)


for A in range(1000, -1000, -1):
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break