from turtle import *
screensize(5000,5000)
m=20
lt=90
tracer(False)
for i in range(2):
    fd(14*m)
    left(270)
    bk(12*m)
    rt(90)
up()
fd(9*m)
rt(90)
bk(7*m)
left(90)
down()
for i in range(2):
    fd(13*m)
    rt(90)
    fd(6*m)
    rt(90)
up()
for x in range(-10,25):
    for y in range(-10, 20):
        goto(x*m,y*m)
        dot(4,"orange")
update()
done()