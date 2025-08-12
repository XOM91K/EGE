from turtle import *
shape('turtle')
lt(90)
tracer(0)
m = 15
for x in range(3):
    fd(7*m)
    rt(90)
    fd(12 * m)
    rt(90)
up()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
down()
for x in range(4):
    fd(83 * m)
    rt(90)
    fd(77 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(7, 'red')
done()