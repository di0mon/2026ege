print("x y w z")
for x in 0, 1:
    for y in range(2):
        for w in (0, 1):
            for z in [0, 1]:
                f = (not x and not y) or (y == w) or z
                if not f:
                    print(x,y,w,z)