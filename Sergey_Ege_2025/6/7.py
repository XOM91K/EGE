from turtle import *

speed(1000)
left(90)
tracer(0)
m = 10
down()
for x in range(3):
    fd(45 * m)
    right(90)
    fd(13 * m)
    right(90)
up()
bk(2 * m)
right(90)
fd(4 * m)
left(90)
down()
for x in range(4):
    fd(76 * m)
    right(90)
    fd(72 * m)
    right(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'red')
done()
