from turtle import *
shape('turtle')
speed(1000)
tracer(0)
m = 10
lt(90)
for x in range(4):
    fd(28 * m)
    rt(90)
    fd(26 * m)
    rt(90)
up()
fd(8 * m)
rt(90)
fd(7 * m)
lt(90)
down()
for x in range(4):
    fd(67 * m)
    rt(90)
    fd(98 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'red')
done()