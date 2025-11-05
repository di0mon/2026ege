from turtle import *
screensize(5000,5000)
tracer(False)
m = 10
lt(90)

for i in range(4):
    fd(30*m)
    rt(90)
    fd(48*m)
    rt(90)
up()
fd(27*m)
rt(90)
fd(24*m)
lt(90)
down()

for i in range(4):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)
up()

for x in range(-20,50):
    for y in range(-10,70):
        goto(x*m,y*m)
        dot(4,"orange")
update()
done()
