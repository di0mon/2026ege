from turtle import *
screensize(5000,5000)
tracer(False)
m = 20
lt(90)

for i in range(9):
    fd(27*m)
    rt(90)
    fd(30*m)
    rt(90)
up()
fd(3*m)
rt(90)
fd(6*m)
lt(90)
down()
for i in range(9):
    fd(77 * m)
    rt(90)
    fd(66 * m)
    rt(90)
up()
for x in range(-30,50):
    for y in range(-10, 30):
        goto(x*m,y*m)
        dot(4,"orange")
update()
done()