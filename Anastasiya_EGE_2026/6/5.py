from turtle import *
#shape('turtle')
tracer(0)
lt(90)
m = 15
down()
for x in range(95):
    fd(12*m)
    rt(120)
up()
goto(0, 0)
rt(210)
fd(5*m)
lt(90)
down()
for x in range(95):
    fd(12*m)
    rt(120)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'pink')
done()