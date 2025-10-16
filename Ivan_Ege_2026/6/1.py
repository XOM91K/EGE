from turtle import *
speed(1000)
tracer(0)
lt(90)
m = 40
for x in range(2):
    fd(7 * m)
    rt(90)
    fd(4 * m)
    rt(90)
up()
fd(2 * m)
rt(90)
fd(5 * m)
lt(90)
down()
for x in range(2):
    fd(3 * m)
    rt(90)
    fd(4 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'red')
done()