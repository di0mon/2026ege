from turtle import *
screensize(5000, 5000)
tracer(False)
m = 40
lt(90)
rt(30)
for i in range(3):
    rt(150)
    fd(6*m)
    rt(30)
    fd(12*m)
up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(4,"orange")
update()
done()