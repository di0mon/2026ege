from turtle import*
screensize(5000,5000)
m=20
tracer(False)
lt(90)
for i in range(3):
    fd(39*m)
    rt(90)
    fd(48*m)
    rt(90)
up()
fd(27*m)
rt(90)
fd(24*m)
lt(90)
down()
for i in range(3):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)
up()
for x in range(-10,45):
    for y in range(-10, 20):
        goto(x*m,y*m)
        dot(4,"orange")
update()
done()
