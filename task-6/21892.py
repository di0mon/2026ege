from turtle import *
screensize(5000,5000)
tracer(False)
lt(90)
m=20

rt(90)
for i in range(7):
    rt(45)
    fd(11*m)
    rt(45)
up()
for x in range(-10,10):
    for y in range(-15,10):
        goto(x*m,y*m)
        dot(4,"orange")
update()
done()
