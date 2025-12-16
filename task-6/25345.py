from turtle import *
tracer(False)
screensize(5000,5000)
m=20
lt(90)

for i in range(6):
    fd(33*m)
    rt(90)
    fd(20*m)
    rt(90)
up()
fd(3 * m)
rt(90)
fd(9 * m)
lt(90)
down()
for i in range(6):
    fd(24*m)
    rt(90)
    fd(25*m)
    rt(90)
up()
for x in range(-0,20):
    for y in range(-0, 30):
        goto(x*m,y*m)
        dot(4,"orange")
update()
done()
