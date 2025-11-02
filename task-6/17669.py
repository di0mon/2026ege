from turtle import *
screensize(5000,5000)
tracer(False)
m = 20

for i in range(4):
    fd(19*m)
    rt(90)
    fd(30)
    rt(90*m)

up()
fd(2*m)
rt(90)
fd(8*m)
lt(90)
down()

for i in range(4):
    fd(93*m)
    rt(90)
    fd(97*m)
    rt(90)
up()
for x in range(-10,100):
    for y in range(-60,0):
        goto(x*m,y*m)
        dot(4, "orange")
update()
done()


