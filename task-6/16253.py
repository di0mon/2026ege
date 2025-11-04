from turtle import *
screensize(20000,20000)
lt(90)
tracer(False)
m = 10
rt(45)
for i in range(10):
    rt(45)
    fd(203*m)
    rt(45)
up()
bk(40*m)
rt(45)
down()
for i in range(5):
    fd(20*m)
    lt(90)
up()
for x in range(150,250):
    for y in range(-200,0):
        goto(x*m,y*m)
        dot(4,"orange")
update()
done()
