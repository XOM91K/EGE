#import turtle
from turtle import *
lt(90)
tracer(0)
m = 15
for x in range(2):
    fd(6 * m)
    rt(90)
    fd(12 * m)
    rt(90)
up()
fd(1 * m)
rt(90)
fd(3 * m)
lt(90)
down()
for x in range(2):
    fd(77 * m)
    rt(90)
    fd(45 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(7, 'blue')
done()