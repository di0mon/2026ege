from turtle import *
screensize(5000, 5000)
tracer(False)
m = 20

rt(270)
for i in range(2):
    fd(8*m)
    rt(120)
rt(120)
for i in range(2):
    rt(120)
    fd(3*m)
    rt(240)
rt(240)
for i in range(2):
    fd(14*m)
    rt(120)
up()

for x in range(-10,15):
    for y in range(-10, 10):
        goto(x*m,y*m)
        dot(4,"orange")
update()
done()


