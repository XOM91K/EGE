from turtle import *
speed(1000)
tracer(0)
left(90)
m = 20
for x in range(7):
    forward(12 * m)
    right(90)
    forward(20 * m)
    right(90)
up()
fd(1  * m)
rt(90)
fd(10 * m)
lt(90)
down()
for x in range(7):
    forward(66 * m)
    right(90)
    forward(92 * m)
    right(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'green')
done()
