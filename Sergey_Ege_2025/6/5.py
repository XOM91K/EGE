from turtle import *
m = 50

speed(1000)
tracer(0)
down()
left(90)
right(30)
for x in range(3):
     right(150)
     fd(6*m)
     right(30)
     fd(12*m)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(2, 'blue')
done()