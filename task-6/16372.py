from turtle import *
screensize(5000, 5000)
tracer(False)
m = 20
lt(90)

for i in range(2):
    fd(23*m)
    lt(90)
    bk(27*m)
    lt(90)
up()
bk(5*m)
rt(90)
fd(11*m)
lt(90)
down()
for i in range(2):
    fd(26*m)
    rt(90)
    fd(32*m)
    rt(90)
up()
for x in range(-10,40):
    for y in range(-10,40):
        goto(x*m,y*m)
        dot(5,"orange")
update()
done()


