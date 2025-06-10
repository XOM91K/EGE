from turtle import *

m = 10
speed(1000)
tracer(0)
down()
for x in range(8):
    forward(16 * m)
    right(90)
    forward(22 * m)
    right(90)

up()
forward(5 * m)
right(90)
forward(5 * m)
left(90)
down()
for x in range(8):
    forward(52 * m)
    right(90)
    forward(77 * m)
    right(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'blue')
done()