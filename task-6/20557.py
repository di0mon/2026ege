from turtle import *
m=20
screensize(5000,5000)
tracer(False)
for i in range(4):
    fd(36*m)
    rt(90)
    fd(41*m)
    rt(90)
up()
rt(90)
fd(20*m)
fd(41*m)
rt(90)
down()
for i in range(4):
    fd(25*m)
    rt(90)
up()
fd(7*m)
rt(90)
fd(7*m)
rt(90)
down()
for i in range(7):
    fd(16*m)
    rt(90)
for x in range(-10,10):
    for y in range(-10,10):
        dot(4,"orange")
update()
done()