from turtle import *
screensize(5000,5000)
tracer(False)
m = 20
lt(90)

for i in range(8):
    fd(16*m)
    rt(90)
    fd(22*m)
    rt(90)
up()
fd(5*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(8):
    fd(52 * m)
    rt(90)
    fd(77 * m)
    rt(90)
up()
for x in range(-10,25):
    for y in range(-10, 20):
        goto(x*m,y*m)
        dot(4,"orange")
update()
done()