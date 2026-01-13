def f(x, y):
    return (x<A) or (y<A) or(x+2*y>50)


for A in range(-1000, 1000):
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break
        #17