from turtle import *
speed(1000)
color('blue', 'violet')
left(90)
m = 40
begin_fill()
for x in range(3):
    forward(13 * m)
    right(120)
end_fill()
ct = 0
for x in range(-100 * m, 100 * m, m):
    for y in range(-100 * m, 100 * m, m):
        t = getcanvas().find_overlapping(x,y,x,y)
        if len(t) == 1 and t[0] == 5:
            print(t)
            ct += 1
print(ct)
done()