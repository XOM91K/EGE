from turtle import *
k = 30
speed(10000)
tracer(0)
shape('turtle')
left(90)
for i in range(95):
    fd(12*k)
    right(120)
up()
goto(0,0)
right(210)
fd(5 * k)
left(90)
down()
for i in range(95):
    fd(12*k)
    right(120)
penup()
for x in range(-20*k,20*k,k):
    for y in range(-20*k,20*k,k):
        goto(x,y)
        dot(5,'blue')
done()