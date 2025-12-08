from turtle import *
screensize(5000,5000)
tracer(False)
m = 20
lt(90)

for i in range(9):
    fd(30*m)
    rt(90)
    fd(12*m)
    rt(90)

up()
lt(270)
fd(5*m)
lt(90)
down()
for i in range(9):
    fd(24*m)
    rt(90)
    fd(28*m)
    rt(90)
up()
for x in range(-30,15):
    for y in range(-10, 30):
        goto(x*m,y*m)
        dot(4,"orange")
update()
done()