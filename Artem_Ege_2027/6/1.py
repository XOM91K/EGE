from turtle import *
tracer(0)
m = 10
lt(90)
for x in range(4):
    fd(19 * m)
    rt(90)
    fd(30 * m)
    rt(90)
up()
fd(2 * m)
rt(90)
fd(8 * m)
lt(90)
down()
for x in range(4):
    fd(93 * m)
    rt(90)
    fd(97 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(4, 'green')
done()
