from turtle import *
k = 20
speed(10000)
tracer(0)
shape('turtle')
left(90)
right(90)
for x in range(8):
    fd(15 * k)
    rt(60)
    fd(10 * k)
    rt(60)
penup()
for x in range(-40*k,40*k,k):
    for y in range(-40*k,40*k,k):
        goto(x,y)
        dot(5,'blue')
done()