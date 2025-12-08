from turtle import *
screensize(5000, 5000)
tracer(False)
lt(90)
m = 20
for i in range(1):
    fd(30*m)
    lt(60)
    fd(24*m)
    rt(240)

fd(54*m)
lt(120)
fd(24*m)
lt(60)

up()
fd(30*m)
rt(90)
fd(20*m)
down()
for i in range(17):
    fd(6 * m)
    lt(90)
    fd(80 * m)
    lt(90)
up()
for x in range(-10,10):
    for y in range(-10, 10):
        goto(x*m,y*m)
        dot(4,"orange")
update()
done()
